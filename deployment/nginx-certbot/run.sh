pip install jinja2-cli
file="/etc/letsencrypt/live/$DOMAIN/fullchain.pem"
if ! [ -e "$file" ]
then
	echo "$file not found."
	jinja2 /cert_folder/nginx/default.j2 -D domain=$DOMAIN -D enable_ssl=false -D enable_redirect=false > /etc/nginx/sites-enabled/default
	service nginx restart
	certbot certonly --webroot -w /my_django_data --agree-tos --email noreply@briteapps.com -d $DOMAIN -n  >> /var/log/certbot-renew.log 2>&1
fi
jinja2 /cert_folder/nginx/default.j2 -D domain=$DOMAIN -D enable_ssl=true -D enable_redirect=$ENABLE_REDIRECT > /etc/nginx/sites-enabled/default
jinja2 /cert_folder/nginx/ssl-params.conf.j2 -D enable_redirect=$ENABLE_REDIRECT > /etc/nginx/snippets/ssl-params.conf
service nginx restart

echo "0 0 * * * /usr/local/bin/certbot renew >> /var/log/certbot-renew.log 2>&1" | crontab
service cron start

tail -f /etc/hosts