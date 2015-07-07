#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, url_for,redirect
import shutil
import markdown
from collections import defaultdict
import codecs
import re, os
from mdx_mathjax import MathJaxExtension
slide =  Blueprint('slide', __name__,  url_prefix='/slides',static_folder='static')

DECK_SETTINGS_RE = {
    'thankyou': u'^%\s*thankyou:(.*)$',
    'thankyou_details': u'^%\s*thankyou_details:(.*)$',
    'title': u'^%\s*title:(.*)$',
    'subtitle': u'^%\s*subtitle:(.*)$',
    'author': u'^%\s*author:(.*)$',
    'contact': u'^%\s*contact:(.*)$',
    'favicon': u'^%\s*favicon:(.*)$',

}
SLIDE_DIR = './content/slides/'
SLIDE_EXT = ".md"
def file_walk(dir):
    slide_arr = []
    
    for name in os.listdir(dir):
        slid_dic = {}
        full_name = os.path.join(dir, name)
        if os.path.isdir(full_name):
            pass
        elif name.endswith(SLIDE_EXT):
            _, settings = parse_deck_settings(codecs.open(full_name, encoding='utf8').read())
            slid_dic['title'] = settings['title']
            slid_dic['path'] = full_name
            slide_arr.append(slid_dic)
    return slide_arr
def parse_deck_settings(md):
    """Parse global settings for the slide deck, such as the author and
    contact information.

    Parameters
    ----------
    md : unicode
        The full markdown source of the slides

    Returns
    -------
    md : unicode
        The markdown source, after the settings have been removed, such
        that they don't get actually put into the slides directly
    settings : dict
        A dict containing the settings. The keys wil be the set of keys
        in DECK_SETTINGS_RE, modulo the keys that were actually parsed
        from the document.
    """
    settings = defaultdict(lambda: [])
    for key, value in DECK_SETTINGS_RE.items():
        found = True
        while found:
            m = re.search(value, md, re.MULTILINE)
            if m:
                settings[key].append(m.group(1))
                md = md.replace(m.group(0), '')
            else:
                found = False

    # if a setting is repeated, we join them together with a <br/> tag
    # in between.
    settings = {k: '<br/>'.join(v) for k, v in settings.items()}

    print("Parsed slide deck settings, and found setting for: {:s}.".format(', '.join(settings.keys())))
    # strip off the newline characters at the beginning and end of the document
    # that might have been left
    md = md.strip()
    md = '\n'+md
    return md, settings
def parse_metadata(section):
    """Given the first part of a slide, returns metadata associated with it."""
    metadata = {}
    metadata_lines = section.split('\n')
    for line in metadata_lines:
        colon_index = line.find(':')
        if colon_index != -1:
            key = line[:colon_index].strip()
            val = line[colon_index + 1:].strip()
            metadata[key] = val

    return metadata

def postprocess_html(html, metadata):
    """Returns processed HTML to fit into the slide template format."""
    if metadata.get('build_lists') and metadata['build_lists'] == 'true':
        html = html.replace('<ul>', '<ul class="build">')
        html = html.replace('<ol>', '<ol class="build">')
    return html


def render_slides(md):
    md, settings = parse_deck_settings(md)
    md = md.replace('\r\n', '\n').replace('\n\r','\n')
    md_slides = md.split('\n---\n') 
  
    #print("Compiled {:d} slides.".format(len(md_slides)))

    slides = []
    # Process each slide separately.
    for md_slide in md_slides:
        slide = {}
        sections = md_slide.split('\n\n')
        # Extract metadata at the beginning of the slide (look for key: value)
        # pairs.
        metadata_section = sections[0]
        metadata = parse_metadata(metadata_section)
        slide.update(metadata)
        remainder_index = metadata and 1 or 0
        # Get the content from the rest of the slide.
        content_section = '\n\n'.join(sections[remainder_index:])
        html = markdown.markdown(content_section, extensions=[MathJaxExtension(), 'markdown.extensions.tables'])
        slide['content'] = postprocess_html(html, metadata)

        slides.append(slide)
    return settings,slides
@slide.route('/figures/<file>')
def home(file):
    return redirect(url_for('static', filename='figures/'+file))
@slide.route('/')
def all_slides():
    slide_arr = file_walk(SLIDE_DIR)
    #pagination = Pagination(page=page, bs_version=3,total=len(g.all), per_page=PER_PAGE, record_name='posts')
    #return render_template('ppt.html', slides=slide_arr, pagination=pagination)
    return render_template('ppt.html', slides=slide_arr)
@slide.route('/<user_url_slug>')
def one_slide(user_url_slug=None):
    # 做些处理
    #print "here", user_url_slug

    #return "hello "+ user_url_slug
    if not user_url_slug:
        markdown_fn = './slides.md'
    else:
        markdown_fn = u'{}/{}'.format(SLIDE_DIR, user_url_slug)
        #markdown_fn ='./slides.md'
    if not os.path.exists(markdown_fn):
        raise OSError('The markdown file "%s" could not be found.' % markdown_fn)
    md = codecs.open(markdown_fn, encoding='utf8').read()
    settings, slides = render_slides(md)
    return render_template('base_slide.html', slides=slides, settings=settings)

if __name__ == '__main__':
    markdown_fn = './slides.md'
    if not os.path.exists(markdown_fn):
        raise OSError('The markdown file "%s" could not be found.' % markdown_fn)
    md = codecs.open(markdown_fn, encoding='utf8').read()	
    render_slides(md)