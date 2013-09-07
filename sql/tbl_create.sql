Create Table Podcasts
(
	rss_url			VARCHAR(256),
	PRIMARY KEY (rss_url)
);

Create Table Episodes
(
  rss_url			VARCHAR(256),
	title				VARCHAR(256),
	site_url		VARCHAR(256),
	audio_url		VARCHAR(256),
	pub_date		VARCHAR(256)	
);
