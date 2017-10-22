server {
  server_name audit.quicksave.io;

  listen 0.0.0.0:80;
  listen [::]:80;

  location / {
    proxy_pass http://0.0.0.0:13666;
  }
}
