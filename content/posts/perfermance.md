title: 性能评估
date: 2015-5-13
tags: 工作
summary: ET性能风险评估

# ET模块8张表

* ET_AIRPORTCONTROL
* ET_FORMID
* ET_ITINERARY
* ET_OPERATINGFLIGHT
* ET_ORIGINALISSUE
* ET_TICKET
* ET_UPDATEHISTORY
* ET_VOLUNTARY


sql语句如下:

 	-- Create table
	create table ET_AIRPORTCONTROL
	(
	  LKEY NUMBER(16) not null,
	  TKNB CHAR(13) not null,
	  CNBR NUMBER(3) not null,
	  ACAL CHAR(3),
	  ASAC CHAR(16),
	  TEXT VARCHAR2(200)
	)
	tablespace OPET_CA_DATA
	  pctfree 10
	  initrans 1
	  maxtrans 255
	  storage
	  (
	initial 64K
	minextents 1
	maxextents unlimited
	  );
	-- Create/Recreate primary, unique and foreign key constraints 
	alter table ET_AIRPORTCONTROL
	  add constraint UNIQUE_ET_AC_TKNBCNBR unique (TKNB, CNBR);
	-- Create/Recreate indexes 
	create index GLOBAL_ET_AC_TKNBCNBR on ET_AIRPORTCONTROL (TKNB, CNBR)
	  tablespace OPET_CA_INDX
	  pctfree 10
	  initrans 2
	  maxtrans 255
	  storage
	  (
	initial 64K
	minextents 1
	maxextents unlimited
	  );
	-- Grant/Revoke object privileges 
	grant select on ET_AIRPORTCONTROL to ETS_DETR;
	grant select on ET_AIRPORTCONTROL to OPENET_COMMON;
	
	
	-- Create table
	create table ET_FORMID
	(
	  LKEY NUMBER(16) not null,
	  TKNB CHAR(13) not null,
	  CNBR NUMBER(3),
	  FITP NUMBER(3),
	  TEXT VARCHAR2(100) not null
	)
	partition by hash (TKNB)
	(
	  partition PAR_DATA_01
	tablespace OPET_CA_PAR1_DATA,
	  partition PAR_DATA_02
	tablespace OPET_CA_PAR2_DATA,
	  partition PAR_DATA_03
	tablespace OPET_CA_PAR3_DATA,
	  partition PAR_DATA_04
	tablespace OPET_CA_PAR4_DATA
	);
	-- Create/Recreate indexes 
	create index GLOBAL_ET_FORMID_TEXT on ET_FORMID (TEXT);
	create index GLOBAL_ET_FORMID_TKNB on ET_FORMID (TKNB);
	-- Grant/Revoke object privileges 
	grant select on ET_FORMID to ETS_DETR;
	grant select on ET_FORMID to OPENET_COMMON;

	create table ET_ITINERARY
	(
	  LKEY NUMBER(16) not null,
	  TKNB CHAR(13) not null,
	  CNBR NUMBER(3) not null,
	  ETKT NUMBER(1),
	  PTKT NUMBER(1),
	  OPEN NUMBER(1),
	  STPC NUMBER(1),
	  NITE NUMBER(1),
	  QSTP NUMBER(1),
	  QSEL NUMBER(1),
	  CMBS NUMBER(1),
	  PREI NUMBER(1),
	  ARCH NUMBER(1),
	  CLTN NUMBER(1),
	  CLTP NUMBER(1),
	  MCOI NUMBER(1),
	  BWLP NUMBER(1),
	  RCBF NUMBER(1),
	  RCAF NUMBER(1),
	  PRTC NUMBER(1),
	  ACSN NUMBER(1),
	  CSID NUMBER(1),
	  CDSH NUMBER(1),
	  CPPN NUMBER(1),
	  OFL2 NUMBER(1),
	  FLTN CHAR(4),
	  FLTA CHAR(1),
	  SEGN NUMBER(3),
	  FSTA CHAR(2),
	  ORIG CHAR(3),
	  DCH1 NUMBER(1),
	  DDAT DATE,
	  DEST CHAR(3),
	  IDAY NUMBER(2),
	  BKDT DATE,
	  DTME CHAR(4),
	  ATME CHAR(4),
	  ALC1 CHAR(2),
	  CSTA CHAR(3),
	  ALC2 CHAR(2),
	  CLAS CHAR(1),
	  NVBF DATE,
	  NVAF DATE,
	  BAGA CHAR(12),
	  QRTG NUMBER(3),
	  ACLA CHAR(1),
	  ACST NUMBER(3),
	  BORD NUMBER(6),
	  BCNT NUMBER(6),
	  BWGT NUMBER(6),
	  PNR1 CHAR(8),
	  PNR2 CHAR(3),
	  MRL1 CHAR(8),
	  MRL2 CHAR(3),
	  FBAS VARCHAR2(20),
	  NFMT NUMBER(1),
	  NFMR NUMBER(1),
	  SACS NUMBER(1),
	  ELOC NUMBER(1),
	  SYNC CHAR(1),
	  ADAT DATE,
	  DCH2 NUMBER(1),
	  EXPS NUMBER(1),
	  EWAI NUMBER(1),
	  CZVE NUMBER(1),
	  TSAL NUMBER(1),
	  INVL NUMBER(1),
	  IVCC NUMBER(1),
	  PFSI NUMBER(1)
	)
	partition by hash (TKNB)
	(
	  partition PAR_DATA_01
	    tablespace OPET_CA_PAR1_DATA,
	  partition PAR_DATA_02
	    tablespace OPET_CA_PAR2_DATA,
	  partition PAR_DATA_03
	    tablespace OPET_CA_PAR3_DATA,
	  partition PAR_DATA_04
	    tablespace OPET_CA_PAR4_DATA
	);
	-- Create/Recreate primary, unique and foreign key constraints 
	alter table ET_ITINERARY
	  add constraint PK_ET_ITINERARY_TKNBCNBR primary key (TKNB, CNBR);
	-- Create/Recreate indexes 
	create index GLOBAL_ET_ITINERARY_CSTA on ET_ITINERARY (CSTA)
	  tablespace OPET_CA_INDX
	  pctfree 10
	  initrans 2
	  maxtrans 255
	  storage
	  (
	    initial 64K
	    minextents 1
	    maxextents unlimited
	  );
	create index GLOBAL_ET_ITINERARY_DDATFLTN on ET_ITINERARY (DDAT, FLTN);
	create index GLOBAL_ET_ITINERARY_MRL1 on ET_ITINERARY (MRL1);
	create index GLOBAL_ET_ITINERARY_ORIGDEST on ET_ITINERARY (ORIG, DEST);
	create index GLOBAL_ET_ITINERARY_PNR1 on ET_ITINERARY (PNR1);
	create index GLOBAL_ET_ITINERARY_TKNBCNBR on ET_ITINERARY (TKNB, CNBR);
	-- Grant/Revoke object privileges 
	grant select on ET_ITINERARY to ETS_DETR;
	grant select on ET_ITINERARY to OPENET_COMMON;


	
	-- Create table
	create table ET_OPERATINGFLIGHT
	(
	  LKEY NUMBER(16) not null,
	  TKNB CHAR(13) not null,
	  CNBR NUMBER(3) not null,
	  OFAC CHAR(3),
	  MKFL NUMBER(1),
	  OFFN CHAR(4),
	  OFFS CHAR(1),
	  OFCL CHAR(1)
	)
	tablespace OPET_CA_DATA
	  pctfree 10
	  initrans 1
	  maxtrans 255
	  storage
	  (
	initial 64K
	minextents 1
	maxextents unlimited
	  );
	-- Create/Recreate primary, unique and foreign key constraints 
	alter table ET_OPERATINGFLIGHT
	  add constraint UNIQUE_ET_OF_TKNBCNBR unique (TKNB, CNBR);
	-- Create/Recreate indexes 
	create index GLOBAL_ET_OF_TKNBCNBR on ET_OPERATINGFLIGHT (TKNB, CNBR)
	  tablespace OPET_CA_INDX
	  pctfree 10
	  initrans 2
	  maxtrans 255
	  storage
	  (
	initial 64K
	minextents 1
	maxextents unlimited
	  );
	-- Grant/Revoke object privileges 
	grant select on ET_OPERATINGFLIGHT to ETS_DETR;
	grant select on ET_OPERATINGFLIGHT to OPENET_COMMON;
	
	
	-- Create table
	create table ET_ORIGINALISSUE
	(
	  LKEY   NUMBER(16) not null,
	  TKNB   CHAR(13) not null,
	  KPTA   NUMBER(1),
	  OIET   NUMBER(1),
	  COPN   VARCHAR2(16),
	  OIDN   CHAR(14),
	  OICY   CHAR(3),
	  PTAC   NUMBER(3),
	  OIDT   CHAR(6),
	  OISN   CHAR(8),
	  IEDNCJ VARCHAR2(200)
	)
	tablespace OPET_CA_DATA
	  pctfree 10
	  initrans 1
	  maxtrans 255
	  storage
	  (
	initial 64K
	minextents 1
	maxextents unlimited
	  );
	-- Create/Recreate primary, unique and foreign key constraints 
	alter table ET_ORIGINALISSUE
	  add constraint UNIQUE_ET_OI_TKNB unique (TKNB);
	-- Create/Recreate indexes 
	create index GLOBAL_ET_OI_TKNB on ET_ORIGINALISSUE (TKNB)
	  tablespace OPET_CA_INDX
	  pctfree 10
	  initrans 2
	  maxtrans 255
	  storage
	  (
	initial 64K
	minextents 1
	maxextents unlimited
	  );
	-- Grant/Revoke object privileges 
	grant select on ET_ORIGINALISSUE to ETS_DETR;
	grant select on ET_ORIGINALISSUE to OPENET_COMMON;
	
	-- Create table
	create table ET_TICKET
	(
	  LKEY  NUMBER(16) not null,
	  TKNB  CHAR(13) not null,
	  NDOB  DATE,
	  SURN  VARCHAR2(64),
	  GIVN  VARCHAR2(60),
	  PTYP  VARCHAR2(10),
	  PAGE  VARCHAR2(10),
	  PCCR  NUMBER(1),
	  ENDR  NUMBER(1),
	  TSEG  NUMBER(3),
	  DTYP  CHAR(1),
	  DTIS  DATE,
	  JORG  CHAR(3),
	  ISSL  NUMBER(1),
	  ISTI  NUMBER(1),
	  TKTP  NUMBER(1),
	  IDPR  NUMBER(1),
	  INFP  NUMBER(1),
	  OPAC  NUMBER(1),
	  TIME  CHAR(4),
	  JDST  CHAR(3),
	  TYGN  NUMBER(1),
	  TYCT  NUMBER(1),
	  DVTP  NUMBER(1),
	  FRML  NUMBER(1),
	  DISP  NUMBER(1),
	  RCPT  NUMBER(1),
	  SNUM  NUMBER(2),
	  STOT  NUMBER(2),
	  CRTC  CHAR(3),
	  BKAL  CHAR(2),
	  CRTO  NUMBER(6),
	  AGTS  NUMBER(6),
	  FION  VARCHAR2(8),
	  TCOF  VARCHAR2(100),
	  ENIF  VARCHAR2(150),
	  PFLAG NUMBER(1),
	  EOVF  NUMBER(1),
	  REIS  NUMBER(1),
	  TKIN  NUMBER(1),
	  OMSG  NUMBER(1),
	  FNIT  NUMBER(1),
	  FNBT  NUMBER(1),
	  ADC5  NUMBER(1),
	  FFLD  CHAR(1),
	  FCUR  CHAR(3),
	  FAMT  CHAR(8),
	  TFLD  CHAR(1),
	  TCUR  CHAR(3),
	  TAMT  CHAR(8),
	  FANF  VARCHAR2(100),
	  TAXF  VARCHAR2(3000),
	  FACF  VARCHAR2(500),
	  FOPF  VARCHAR2(200),
	  CRSC  CHAR(3),
	  CRSL  VARCHAR2(25),
	  IDTP  CHAR(3),
	  TAID  CHAR(8),
	  IHID  CHAR(9),
	  OARQ  CHAR(9),
	  IHIB  CHAR(9),
	  CRSN  CHAR(4),
	  ICTY  CHAR(3),
	  ORGT  CHAR(1),
	  CHNN  VARCHAR2(64),
	  CHNE  VARCHAR2(150),
	  AIRP  NUMBER(1),
	  UMCH  NUMBER(1),
	  BANK  NUMBER(1),
	  PRIC  NUMBER(2),
	  SPCA  NUMBER(1),
	  NRE2  NUMBER(1),
	  CZRQ  NUMBER(1),
	  MNVD  NUMBER(1),
	  FCMN  NUMBER(1),
	  CZWB  NUMBER(1),
	  IDGP  NUMBER(1)
	)
	partition by hash (TKNB)
	(
	  partition PAR_DATA_01
	tablespace OPET_CA_PAR1_DATA,
	  partition PAR_DATA_02
	tablespace OPET_CA_PAR2_DATA,
	  partition PAR_DATA_03
	tablespace OPET_CA_PAR3_DATA,
	  partition PAR_DATA_04
	tablespace OPET_CA_PAR4_DATA
	);
	-- Create/Recreate primary, unique and foreign key constraints 
	alter table ET_TICKET
	  add constraint PK_ET_TICKET_TKNB primary key (TKNB);
	-- Create/Recreate indexes 
	create index GLOBAL_ET_TICKET_DTIS on ET_TICKET (DTIS);
	create index GLOBAL_ET_TICKET_GIVN on ET_TICKET (GIVN);
	create index GLOBAL_ET_TICKET_IHID on ET_TICKET (IHID);
	create index GLOBAL_ET_TICKET_OPAC on ET_TICKET (OPAC)
	  tablespace OPET_CA_INDX
	  pctfree 10
	  initrans 2
	  maxtrans 255
	  storage
	  (
	initial 64K
	minextents 1
	maxextents unlimited
	  );
	create index GLOBAL_ET_TICKET_PFLAG on ET_TICKET (PFLAG)
	  tablespace OPET_CA_INDX
	  pctfree 10
	  initrans 2
	  maxtrans 255
	  storage
	  (
	initial 64K
	minextents 1
	maxextents unlimited
	  );
	create index GLOBAL_ET_TICKET_SURN on ET_TICKET (SURN);
	create index GLOBAL_ET_TICKET_TKNB on ET_TICKET (TKNB);
	-- Grant/Revoke object privileges 
	grant select on ET_TICKET to ETS_DETR;
	grant select on ET_TICKET to OPENET_COMMON;
	
	
	-- Create table
	create table ET_UPDATEHISTORY
	(
	  LKEY NUMBER(16) not null,
	  TKNB CHAR(13) not null,
	  CNBR NUMBER(3),
	  HCNB NUMBER(3),
	  HTYP NUMBER(3),
	  RMXL NUMBER(1),
	  CSCC NUMBER(1),
	  TAUP NUMBER(1),
	  ACFL NUMBER(1),
	  NFMT NUMBER(1),
	  SACS NUMBER(1),
	  HDAT DATE,
	  HCTC VARCHAR2(25),
	  HAAL CHAR(3),
	  HOFC CHAR(8),
	  HAGT CHAR(6),
	  TEXT VARCHAR2(100),
	  TRID VARCHAR2(20),
	  BTAI CHAR(15),
	  SVCT NUMBER(3),
	  IHID CHAR(9),
	  HSFS NUMBER(1),
	  HSIL NUMBER(1),
	  MDAT DATE,
	  MTIM VARCHAR2(8)
	)
	partition by hash (TKNB)
	(
	  partition PAR_DATA_01
	tablespace OPET_CA_PAR1_DATA,
	  partition PAR_DATA_02
	tablespace OPET_CA_PAR2_DATA,
	  partition PAR_DATA_03
	tablespace OPET_CA_PAR3_DATA,
	  partition PAR_DATA_04
	tablespace OPET_CA_PAR4_DATA
	);
	-- Create/Recreate indexes 
	create index GLOBAL_ET_UPDATEHISTORY_HDAT on ET_UPDATEHISTORY (HDAT);
	create index GLOBAL_ET_UPDATEHISTORY_TKNB on ET_UPDATEHISTORY (TKNB);
	-- Grant/Revoke object privileges 
	grant select on ET_UPDATEHISTORY to ETS_DETR;
	grant select on ET_UPDATEHISTORY to OPENET_COMMON;
	
	
	-- Create table
	create table ET_VOLUNTARY
	(
	  LKEY NUMBER(16) not null,
	  TKNB CHAR(13) not null,
	  CNBR NUMBER(3) not null,
	  VEAL CHAR(3),
	  VEID NUMBER(1),
	  VEA2 CHAR(2),
	  VEA3 CHAR(2)
	)
	tablespace OPET_CA_DATA
	  pctfree 10
	  initrans 1
	  maxtrans 255
	  storage
	  (
	initial 64K
	minextents 1
	maxextents unlimited
	  );
	-- Create/Recreate primary, unique and foreign key constraints 
	alter table ET_VOLUNTARY
	  add constraint UNIQUE_ET_VT_TKNBCNBR unique (TKNB, CNBR);
	-- Create/Recreate indexes 
	create index GLOBAL_ET_VT_TKNBCNBR on ET_VOLUNTARY (TKNB, CNBR)
	  tablespace OPET_CA_INDX
	  pctfree 10
	  initrans 2
	  maxtrans 255
	  storage
	  (
	initial 64K
	minextents 1
	maxextents unlimited
	  );
	-- Grant/Revoke object privileges 
	grant select on ET_VOLUNTARY to ETS_DETR;
	
# 性能风险评估

## 并发
并发量有2K~3K，在高并发的情况下，可能存在:

* 数据库宕机
* 内存占用过大，或者泄漏
* 磁盘空间占用过大
* SQL语句阻塞

## 类型

表的类型主要有NUMBER和CHAR,VARCHAR,DATE四种类型。oracle的NUMBER和CHAR,VARCHAR与DM7兼容,
可能存在的风险:

* oracle DATE类型与DM7的datetime类型对应，可能存在长度，格式不一致的问题。

## 兼容性

已经和民航信息确认，ET的业务均是应用采用sql语句完成，没有涉及存储过程，包等。因此，可能存在的风险有：

* DM7不支持oracle的函数、语法
* 查询语句执行计划不恰当导致性能低下
* 结果集与oracle不一致










