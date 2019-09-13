/*
SQLyog Ultimate v12.5.0 (64 bit)
MySQL - 5.7.25 : Database - video
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`video` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `video`;

/*Table structure for table `source` */

DROP TABLE IF EXISTS `source`;

CREATE TABLE `source` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  `info` varchar(256) DEFAULT NULL,
  `label` varchar(200) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `source` */

/*Table structure for table `source_detail` */

DROP TABLE IF EXISTS `source_detail`;

CREATE TABLE `source_detail` (
  `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(100) DEFAULT NULL,
  `url` varchar(500) DEFAULT NULL,
  `info` varchar(256) DEFAULT NULL,
  `source_id` bigint(20) DEFAULT NULL,
  `create_time` datetime DEFAULT NULL,
  `update_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=utf8;

/*Data for the table `source_detail` */

insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (1,'第1集','/index.php/vod/play/id/52871/sid/1/nid/1.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (2,'第2集','/index.php/vod/play/id/52871/sid/1/nid/2.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (3,'第3集','/index.php/vod/play/id/52871/sid/1/nid/3.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (4,'第4集','/index.php/vod/play/id/52871/sid/1/nid/4.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (5,'第5集','/index.php/vod/play/id/52871/sid/1/nid/5.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (6,'第6集','/index.php/vod/play/id/52871/sid/1/nid/6.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (7,'第7集','/index.php/vod/play/id/52871/sid/1/nid/7.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (8,'第8集','/index.php/vod/play/id/52871/sid/1/nid/8.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (9,'第9集','/index.php/vod/play/id/52871/sid/1/nid/9.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (10,'第10集','/index.php/vod/play/id/52871/sid/1/nid/10.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (11,'第11集','/index.php/vod/play/id/52871/sid/1/nid/11.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (12,'第12集','/index.php/vod/play/id/52871/sid/1/nid/12.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (13,'第13集','/index.php/vod/play/id/52871/sid/1/nid/13.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (14,'第14集','/index.php/vod/play/id/52871/sid/1/nid/14.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (15,'第15集','/index.php/vod/play/id/52871/sid/1/nid/15.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (16,'第16集','/index.php/vod/play/id/52871/sid/1/nid/16.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (17,'第17集','/index.php/vod/play/id/52871/sid/1/nid/17.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (18,'第18集','/index.php/vod/play/id/52871/sid/1/nid/18.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (19,'第19集','/index.php/vod/play/id/52871/sid/1/nid/19.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (20,'第20集','/index.php/vod/play/id/52871/sid/1/nid/20.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (21,'第21集','/index.php/vod/play/id/52871/sid/1/nid/21.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (22,'第22集','/index.php/vod/play/id/52871/sid/1/nid/22.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (23,'第23集','/index.php/vod/play/id/52871/sid/1/nid/23.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (24,'第24集','/index.php/vod/play/id/52871/sid/1/nid/24.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (25,'第01集','http://byzfwl.zdqbrya.9izhuiju.com/index.php/vod/play/id/53349/sid/1/nid/1.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (26,'第02集','http://byzfwl.zdqbrya.9izhuiju.com/index.php/vod/play/id/53349/sid/1/nid/2.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (27,'第03集','http://byzfwl.zdqbrya.9izhuiju.com/index.php/vod/play/id/53349/sid/1/nid/3.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (28,'第04集','http://byzfwl.zdqbrya.9izhuiju.com/index.php/vod/play/id/53349/sid/1/nid/4.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (29,'第05集','http://byzfwl.zdqbrya.9izhuiju.com/index.php/vod/play/id/53349/sid/1/nid/5.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (30,'第06集','http://byzfwl.zdqbrya.9izhuiju.com/index.php/vod/play/id/53349/sid/1/nid/6.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (31,'第07集','http://byzfwl.zdqbrya.9izhuiju.com/index.php/vod/play/id/53349/sid/1/nid/7.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (32,'第08集','http://byzfwl.zdqbrya.9izhuiju.com/index.php/vod/play/id/53349/sid/1/nid/8.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (33,'第09集','http://byzfwl.zdqbrya.9izhuiju.com/index.php/vod/play/id/53349/sid/1/nid/9.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (34,'第10集','http://byzfwl.zdqbrya.9izhuiju.com/index.php/vod/play/id/53349/sid/1/nid/10.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (35,'第11集','http://byzfwl.zdqbrya.9izhuiju.com/index.php/vod/play/id/53349/sid/1/nid/11.html',NULL,NULL,NULL,NULL);
insert  into `source_detail`(`id`,`title`,`url`,`info`,`source_id`,`create_time`,`update_time`) values (36,'第12集','http://byzfwl.zdqbrya.9izhuiju.com/index.php/vod/play/id/53349/sid/1/nid/12.html',NULL,NULL,NULL,NULL);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
