# djangofileupload
file upload by using simpe way and database

      DROP TABLE IF EXISTS `djangoapp`.`fileupload_document`;
      CREATE TABLE  `djangoapp`.`fileupload_document` (
        `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
        `description` varchar(45) NOT NULL,
        `document` blob NOT NULL,
        `uploaded_at` datetime NOT NULL,
        PRIMARY KEY (`id`)
      ) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
