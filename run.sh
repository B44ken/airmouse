SITE='vps.p27.ca'
export CERT="/etc/letsencrypt/live/$SITE/cert.pem"
export KEY="/etc/letsencrypt/live/$SITE/privkey.pem"

sudo flask run --host 0.0.0.0 --cert $CERT --key $KEY --port 443
