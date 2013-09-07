Create Table Podcasts
(
	podcast			VARCHAR(256),
	PRIMARY KEY (podcast)
);

Create Table Episodes
(
	podcast			VARCHAR(256),
	title				VARCHAR(256),
	site_url		VARCHAR(256),
	audio_url		VARCHAR(256),
	pubdate			TIMESTAMP,
	PRIMARY KEY (title)
);
