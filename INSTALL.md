
Environment variables:
	STARX_ENV: DEV || PROD
	MYSQL_USER: MySQL user
	MYSQL_PASSWORD: MySQL password
	MYSQL_DATABASE: MySQL database

NOTE: your facebook app's
    Settings -> WebSite -> Site URL must the one you are serving form

Your app id needs to be inserted into the database per:
http://www.sarahhagstrom.com/2013/09/the-missing-django-allauth-tutorial/

And your DOMAIN needs to match facebook app doman

UPDATE django_site SET DOMAIN = '127.0.0.1:8000', name = 'Vort' WHERE id=1;
INSERT INTO socialaccount_socialapp (provider, name, secret, client_id, `key`)
VALUES ("facebook", "Facebook", "--put-your-own-app-secret-here--", "--put-your-own-app-id-here--", '');
INSERT INTO socialaccount_socialapp_sites (socialapp_id, site_id) VALUES (1,1);

Also, site ID must be defined in settings and match the one here.
