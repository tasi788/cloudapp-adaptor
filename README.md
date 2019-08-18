# cloudapp adaptor

a simple server adapting file request to [CloudApp](https://getcloudapp.com) using API.

## Install (Docker)  
`docker-compose up -d`

## How 2 use

### endpoint: domain.com  

> ### upload file  
 - `HTTP method`  
   using HTTP `POST` with `form-data`

 - `auth` (str)  
   verify uploader

 - `output` (str)  
  if set to `full` it will return full of result in json back

 - `file` (file)  
  attach file which you want to upload
  #### example

> ### add auth key
 - `HTTP method`  
  using HTTP `POST` with `form-data`

 - `tdc` (str)
  set in config.cfg
 
 - `name` (str)
  set for auth key name

 - `auth` (str)  
  set for auth key, generate from bitwarden, lastpass, 1password are recommanded.

