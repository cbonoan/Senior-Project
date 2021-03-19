-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: mindsanctuary
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `adminid` int unsigned NOT NULL,
  `userid` int unsigned NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`adminid`),
  UNIQUE KEY `adminid_UNIQUE` (`adminid`),
  UNIQUE KEY `userid_UNIQUE` (`userid`),
  CONSTRAINT `userid` FOREIGN KEY (`userid`) REFERENCES `user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77493 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (77492,77492);
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `admin_BEFORE_INSERT` BEFORE INSERT ON `admin` FOR EACH ROW BEGIN
set new.adminid = new.userid;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `articles`
--

DROP TABLE IF EXISTS `articles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `articles` (
  `article_emotion` varchar(45) NOT NULL,
  `article_title` varchar(255) NOT NULL,
  PRIMARY KEY (`article_title`,`article_emotion`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `articles`
--

LOCK TABLES `articles` WRITE;
/*!40000 ALTER TABLE `articles` DISABLE KEYS */;
INSERT INTO `articles` VALUES ('',''),('loving',' https://tinybuddha.com/blog/how-to-feel-more-loved-9-tips-for-deep-connection/'),('aggressive','http://www.psychedinsanfrancisco.com/on-aggression/'),('nostalgic','https://blog.freepeople.com/2015/11/10-thingsto-feeling-nostalgic/'),('indifferent','https://blog.heartmanity.com/empathy-is-the-antidote-for-apathy-and-indifference'),('enthusiastic','https://enthousiasme.info/en/information/articles/?article=54'),('fragile','https://exploringyourmind.com/emotional-fragility-keys-understanding-ego/'),('inspired','https://hbr.org/2011/11/why-inspiration-matters'),('rejected','https://ideas.ted.com/why-rejection-hurts-so-much-and-what-to-do-about-it/'),('embarrassed','https://landit.com/articles/6-ways-to-move-past-an-embarrassing-moment'),('reserved','https://liveboldandbloom.com/11/personality-types/reserved-personality'),('nurtured','https://medium.com/@christinekathrynreber/identifying-what-makes-you-feel-nurtured-is-the-first-step-to-self-care-54e2a9dc8799'),('ridiculed','https://medium.com/@onyourplate/how-to-deal-with-ridicule-without-getting-depressed-6228816e3f0d'),('inquisitive','https://medium.com/tan-kit-yung/on-the-importance-of-being-inquisitive-8b1f5aec91b1'),('scared','https://mhanational.org/what-can-i-do-when-im-afraid'),('accomplished','https://michaelhyatt.com/every-day-accomplishment/'),('grateful','https://positivepsychology.com/neuroscience-of-gratitude/'),('powerless','https://psychcentral.com/blog/how-to-empower-yourself-when-you-feel-powerless-and-helpless#6'),('thankful','https://smartleadershiphut.com/motivation/grateful-vs-thankful/'),('inferior','https://socialpronow.com/blog/feeling-inferior/'),('reclusive','https://socialpronow.com/blog/stop-being-a-loner/'),('stimulated','https://stevepavlina.com/blog/2014/12/stimulation/'),('melancholy','https://thedailymind.com/simple-guide-overcoming-melancholy/'),('satisfied','https://time.com/25208/how-to-be-more-satisfied-with-your-life-5-steps-proven-by-research/'),('confident','https://tinybuddha.com/blog/8-ways-to-be-more-confident-live-the-life-of-your-dreams/'),('successful','https://tinybuddha.com/blog/what-really-makes-us-feel-successful-in-life/'),('passionate','https://www.aconsciousrethink.com/7912/things-passionate-about/'),('calm','https://www.alustforlife.com/tools/mental-health/how-to-embrace-and-inhabit-the-calmness-habit'),('reminiscent','https://www.countrycourtcare.co/support-advice/ten-reasons-why-reminiscing-is-important/'),('hyped','https://www.eofire.com/get-fired-up-now/'),('abandonded','https://www.gaiam.com/blogs/discover/how-to-overcome-the-feeling-of-abandonment'),('content','https://www.greatbigminds.com/are-you-feeling-content-5-signs-you-are-truly-content-with-life/'),('sad','https://www.gundersenhealth.org/health-wellness/live-happy/healthy-ways-to-deal-with-sadness/'),('bitter','https://www.harleytherapy.co.uk/counselling/12-steps-to-overcoming-bitterness.htm'),('nervous','https://www.healthline.com/health/anxiety/nervousness#tips-to-overcome-nervousness'),('confused','https://www.healthline.com/health/confusion'),('depressed','https://www.healthline.com/health/depression/how-to-fight-depression'),('insecure','https://www.healthline.com/health/how-to-stop-being-insecure'),('betrayed','https://www.healthline.com/health/mental-health/betrayal-trauma#signs-and-symptoms'),('distant','https://www.healthline.com/health/mental-health/emotional-detachment'),('tired','https://www.healthline.com/nutrition/10-reasons-you-are-tired\n'),('worried','https://www.helpguide.org/articles/anxiety/how-to-stop-worrying.htm\n'),('driven','https://www.inc.com/peter-economy/12-habits-of-extraordinarily-motivated-people.html'),('self-assured','https://www.lifehack.org/698438/how-to-be-more-self-assured'),('eager','https://www.lifehack.org/854928/eager-to-learn'),('excited','https://www.lifehack.org/articles/communication/10-simple-reasons-you-should-feel-excited-about-your-day.html'),('bored','https://www.lifehack.org/articles/featured/10-ways-to-conquer-boredom-and-feeling-too-busy.html'),('curious','https://www.lifehack.org/articles/productivity/4-reasons-why-curiosity-is-important-and-how-to-develop-it.html'),('independent','https://www.melyssagriffin.com/be-more-independent/'),('desirous','https://www.memoirsofanaddictedbrain.com/connect/feeling-guilty-and-desirous/\n'),('enamored','https://www.mic.com/articles/115482/there-s-an-awesome-stage-between-like-and-love-and-this-is-what-it-s-called'),('intimate','https://www.mindbodygreen.com/articles/types-of-intimacy-besides-sex'),('artistic','https://www.npr.org/sections/health-shots/2020/01/11/795010044/feeling-artsy-heres-how-making-art-helps-your-brain'),('violated','https://www.positivelypositive.com/2017/02/26/acknowledge-youve-been-violated-and-step-into-your-soul-purpose/'),('jealous','https://www.psychalive.org/how-to-deal-with-jealousy/'),('lonely','https://www.psychologytoday.com/us/blog/click-here-happiness/201902/feeling-lonely-discover-18-ways-overcome-loneliness'),('weak','https://www.psychologytoday.com/us/blog/emotional-mastery/201903/how-do-you-develop-emotionally-strong-person'),('accepted','https://www.psychologytoday.com/us/blog/evolution-the-self/200809/the-path-unconditional-self-acceptance'),('provoked','https://www.psychologytoday.com/us/blog/evolution-the-self/200910/disarming-your-buttons-how-not-get-provoked-pt-1-4'),('apathetic','https://www.psychologytoday.com/us/blog/evolution-the-self/201604/the-curse-apathy-sources-and-solutions'),('playful','https://www.psychologytoday.com/us/blog/having-fun/201508/the-underrated-importance-being-playful'),('trusting','https://www.psychologytoday.com/us/blog/hot-thought/201810/what-is-trust'),('humilated','https://www.psychologytoday.com/us/blog/living-single/201402/10-steps-getting-over-humiliation'),('disrespected','https://www.psychologytoday.com/us/blog/out-the-darkness/201201/slighting-the-best-way-respond-feeling-slighted'),('loved','https://www.psychologytoday.com/us/blog/raising-happiness/201602/3-surprising-ways-feel-more-loved'),('fearful','https://www.psychologytoday.com/us/blog/the-angry-therapist/201612/how-stop-being-so-afraid-start-feeling-powerful-alive'),('disillusioned','https://www.psychologytoday.com/us/blog/the-couch/201503/disappointed-disillusioned-8-ways-deal-letdown'),('energetic','https://www.psychologytoday.com/us/blog/the-happiness-project/200911/eight-tips-feeling-more-energetic\n'),('valued','https://www.psychologytoday.com/us/blog/the-i-m-approach/202005/why-do-we-need-feel-valued'),('courageous','https://www.psychologytoday.com/us/blog/the-mindful-self-express/201208/the-six-attributes-courage'),('longing','https://www.psychologytoday.com/us/blog/the-pursuit-peace/201709/longing-more'),('let down','https://www.psychologytoday.com/us/blog/turning-straw-gold/201810/what-do-when-you-feel-let-down-someone'),('frustrated','https://www.psychologytoday.com/us/blog/turning-straw-gold/201909/5-things-try-when-you-re-frustrated'),('threatened','https://www.psychologytoday.com/us/blog/your-wise-brain/201601/what-makes-you-feel-threatened'),('peaceful','https://www.psychologytoday.com/us/blog/your-wise-brain/201611/what-is-your-sense-peace'),('inadequate','https://www.quickanddirtytips.com/health-fitness/mental-health/how-to-stop-feeling-inadequate'),('recreational','https://www.recreation.gov/'),('amused','https://www.richmond-news.com/living/column-the-importance-of-being-amused-3079934'),('humourous','https://www.scienceofpeople.com/how-to-be-funny/'),('distant','https://www.talkspace.com/blog/dealing-with-distant-people/'),('tactile','https://www.thecut.com/2016/05/the-people-who-store-their-emotions-in-their-fingertips.html'),('sensitive','https://www.thegoodtrade.com/features/am-i-too-sensitive'),('hopeful','https://www.theguardian.com/books/2016/jul/15/rebecca-solnit-hope-in-the-dark-new-essay-embrace-unknown'),('creative','https://www.theodysseyonline.com/10-creative-things'),('skeptical','https://www.theschooloflife.com/thebookoflife/emotional-scepticism/'),('hostile','https://www.uofmhealth.org/health-library/anger'),('sleepy','https://www.verywellhealth.com/reasons-why-you-feel-sleepy-3014818'),('angry','https://www.verywellmind.com/5-things-to-do-if-you-feel-angry-5092021\n'),('annoyed','https://www.verywellmind.com/8-things-to-do-if-you-feel-irritable-5081875'),('hopeless','https://www.verywellmind.com/9-things-to-do-if-you-feel-hopeless-5081877'),('vulnerable','https://www.verywellmind.com/fear-of-vulnerability-2671820'),('optimistic','https://www.verywellmind.com/how-to-be-optimistic-4164832'),('relaxed','https://www.verywellmind.com/how-to-become-relaxed-3145059'),('aroused','https://www.verywellmind.com/the-arousal-theory-of-motivation-2795380'),('happy','https://www.verywellmind.com/the-nuances-of-happiness-emotions-beyond-happiness-1717543'),('worthless','https://www.verywellmind.com/things-to-do-if-you-are-feeling-worthless-5087740'),('stressed','https://www.verywellmind.com/ways-to-calm-down-quickly-when-overwhelmed-3145197'),('persecuted','https://www.verywellmind.com/what-are-persecutory-delusions-4586500'),('anxious','https://www.webmd.com/mental-health/features/ways-to-reduce-anxiety\n'),('paranoid','https://www.webmd.com/mental-health/why-paranoid'),('proud','https://www.weforum.org/agenda/2018/03/how-our-emotions-can-help-build-resilient-societies/'),('joyful','https://yogisurprise.com/the-practice-of-being-joyful/\n'),('adventurous','https://zackkanter.com/2012/05/24/bored-stuck-or-just-adventurous-50-randoms-things-to-do/');
/*!40000 ALTER TABLE `articles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `book`
--

DROP TABLE IF EXISTS `book`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `book` (
  `book_emotion` varchar(45) NOT NULL,
  `book_title` varchar(255) NOT NULL,
  PRIMARY KEY (`book_emotion`,`book_title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `book`
--

LOCK TABLES `book` WRITE;
/*!40000 ALTER TABLE `book` DISABLE KEYS */;
INSERT INTO `book` VALUES ('aroused','https://www.amazon.com/Aroused-History-Hormones-Control-Everything/dp/0393239608'),('grateful','https://www.amazon.com/Psychology-Gratitude-Affective-Science/dp/0195150104'),('happy','https://www.amazon.com/Exploring-Happiness-Aristotle-Brain-Science/dp/0300178107'),('hopeful','https://www.amazon.com/Hope-Dark-Untold-Histories-Possibilities/dp/1608465764'),('joyful','https://www.amazon.com/Joyful-Surprising-Ordinary-Extraordinary-Happiness/dp/0316399264'),('loved','https://www.amazon.com/Feeling-Loved-Nurturing-Meaningful-Connections/dp/1941631479'),('loving','https://www.amazon.com/Mathematics-Love-Patterns-Ultimate-Equation/dp/1476784884'),('nostalgic','https://www.amazon.com/Nostalgia-M-G-Vassanji/dp/0385667167'),('proud','https://www.amazon.com/Proud-Fight-Unlikely-American-Dream/dp/0316518964'),('reminiscent','https://www.amazon.com/Reminiscence-story-young-wanted-change/dp/0692775471'),('sensitive','https://www.amazon.com/Sensitive-Self-Michael-Eigen/dp/0819566853');
/*!40000 ALTER TABLE `book` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `feelings`
--

DROP TABLE IF EXISTS `feelings`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `feelings` (
  `user` int unsigned NOT NULL,
  `emotion` varchar(45) NOT NULL,
  `date` varchar(45) NOT NULL,
  PRIMARY KEY (`user`,`date`,`emotion`),
  KEY `emotion` (`emotion`),
  CONSTRAINT `user` FOREIGN KEY (`user`) REFERENCES `user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `feelings`
--

LOCK TABLES `feelings` WRITE;
/*!40000 ALTER TABLE `feelings` DISABLE KEYS */;
INSERT INTO `feelings` VALUES (77492,'angry','2021-03-17'),(77492,'happy','2021-03-19'),(77492,'sad','2021-03-18');
/*!40000 ALTER TABLE `feelings` ENABLE KEYS */;
UNLOCK TABLES;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `feelings_BEFORE_INSERT` BEFORE INSERT ON `feelings` FOR EACH ROW BEGIN
set new.date = curdate();
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;

--
-- Table structure for table `games`
--

DROP TABLE IF EXISTS `games`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `games` (
  `games_emotion` varchar(45) NOT NULL,
  `games_title` varchar(255) NOT NULL,
  PRIMARY KEY (`games_emotion`,`games_title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `games`
--

LOCK TABLES `games` WRITE;
/*!40000 ALTER TABLE `games` DISABLE KEYS */;
INSERT INTO `games` VALUES ('nostalgic','https://www.google.com/doodles/30th-anniversary-of-pac-man');
/*!40000 ALTER TABLE `games` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `movies` (
  `movie_emotion` varchar(45) NOT NULL,
  `movie_title` varchar(255) NOT NULL,
  PRIMARY KEY (`movie_emotion`,`movie_title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `songs`
--

DROP TABLE IF EXISTS `songs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `songs` (
  `songs_emotion` varchar(45) NOT NULL,
  `songs_title` varchar(45) NOT NULL,
  `link` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`songs_emotion`,`songs_title`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `songs`
--

LOCK TABLES `songs` WRITE;
/*!40000 ALTER TABLE `songs` DISABLE KEYS */;
INSERT INTO `songs` VALUES ('apathetic','Lustre - Let go like leaves of Fall','https://www.youtube.com/watch?v=ZCeNHJ8mJI8'),('aroused','Trust - Shoom','https://www.youtube.com/watch?v=RGVmhrfQqzgF'),('calm','Tim Hecker - Boreal Kiss pt.1','https://www.youtube.com/watch?v=ngneYPFkkTQ'),('courageous','Fleet Foxes - Young Man\'s Game','https://www.youtube.com/watch?v=OHsGsMD9wW0'),('driven','Deer Tick - Long Time','https://www.youtube.com/watch?v=yzfkApXfLpI'),('faded','Aftertheparty - Numb','https://www.youtube.com/watch?v=1Zk_D0zkzAc'),('fragile','Pity Sex - Wind Up','https://www.youtube.com/watch?v=XC3r3Jc44LQ\n'),('hopeful','Temper Trap - Sweet Disposition','https://www.youtube.com/watch?v=W-ENipUB8NI'),('hyped','The 1975 - Love it if we made it','https://www.youtube.com/watch?v=GRhUVvUvPuU'),('independent','Tame Impala - Currents','https://www.youtube.com/watch?v=NMRhx71bGo4&list=PLB5vexwf7WGmr_uOM_0BbRPEOA09Blf5Q'),('indifferent','King Krule - Lonely Blue','https://www.youtube.com/watch?v=PN9ND1abjD8'),('lonely','Fleet Foxes - Mykonos','https://www.youtube.com/watch?v=4-IgBcEkXSw\n'),('melancholy','Wilco - Yankee Hotel Foxtrot','https://www.youtube.com/watch?v=3RQcPC8KY_g&list=PLJNbijG2M7OzhPF01zaXVFi3-A5bONW_p'),('nervous','Claude Debussy - Clair de Lune','https://www.youtube.com/watch?v=ea2WoUtbzuw'),('passionate','Postal Service - Give Up','https://www.youtube.com/watch?v=0SIJoBxKtPY&list=PLMynaxX_I0z8VkFLhfDIjM7sf67kHG4_k'),('peaceful','DIIV - For the Guilty','https://www.youtube.com/watch?v=wUW4oBnD_Gg'),('playful','Outkast - Bowtie','https://www.youtube.com/watch?v=CpZzOfgZbgY'),('powerless','Mac Demarco - Let her go','https://www.youtube.com/watch?v=RSACSNBOloo'),('proud','Tiger Army - Outlaw Heart','https://www.youtube.com/watch?v=pkn24yxDoJ4'),('reminiscent','My Bloody Valentine - Loveless','https://www.youtube.com/watch?v=Dq76B2sDpFA'),('reserved','Swans - Bring the Sun','https://www.youtube.com/watch?v=JlqBcXh231g'),('sad','Daniel Blumberg - Minus','https://www.youtube.com/watch?v=tepBgl21g6E'),('satisfied','Sufjan Stevens - Impossible Soul','https://www.youtube.com/watch?v=8R_3mXZBsuU'),('scared','Slightly Stoopid - Collie Man','https://www.youtube.com/watch?v=TLcmtBA-W_s'),('self-assured','The Shins - Simple Song','https://www.youtube.com/watch?v=GyAJ4V06izg'),('sleepy','Persona 5 OST - Beneath the Mask','https://www.youtube.com/watch?v=Uq7kyf1T_lk'),('tactile','Kendrick Lamar - LOVE','https://www.youtube.com/watch?v=XKkV2j9DbIQ'),('weak','Radiohead - Reckoner','https://www.youtube.com/watch?v=pYHEpDnvVPk'),('worried','Smashing Pumpkins - Mayonaise','https://www.youtube.com/watch?v=Vbu_K41efvY');
/*!40000 ALTER TABLE `songs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(45) NOT NULL,
  `password` varchar(100) NOT NULL,
  `email` varchar(45) NOT NULL,
  `name` varchar(45) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `password_UNIQUE` (`password`),
  UNIQUE KEY `email_UNIQUE` (`email`),
  UNIQUE KEY `username_UNIQUE` (`username`),
  UNIQUE KEY `userid_UNIQUE` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=77493 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (4584,'john32','$2b$12$M/QG5fdvWmn875mP/42ViesHCsEiASm3h2Kdeu4JJAVFj6k9zRI06','steven@gmail.com','john steve'),(54166,'charles34','$2b$12$bpia/CiM0.LuQb3i.a4zp.M6JPqBp2dYherSdRqxeA83HblV5vz.a','cbonoan@gmail.com','Charles Bonoan'),(77492,'arvin321','$2b$12$EjJ1xJ.RsAQ8uWOPfedDOexjexi2nFlJSmeEwzkwwDLD9J7ZYBp0G','Shertukde@gmail.com','Arvin Shertukde');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'mindsanctuary'
--

--
-- Dumping routines for database 'mindsanctuary'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-03-19  4:48:20
