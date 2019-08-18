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
  ```shell
  $ curl -X POST \
  https://i.domain.dev \
  -F auth=98TfmKDie6Qz5k8DKGd8AEqgE \
  -F file=@/path/dls/screenshot.png \
  -F output=full
  > {
      "result": {
    "content_url": "http://i.domain.dev/null/screenshot.png",
    "created_at": "2019-08-18T05:26:26Z",
    "favorite": false,
    "id": 101673333,
    "item_type": "image",
    "long_link": true,
    "name": "screenshot.png",
    "redirect_url": null,
    "remote_url": "http://f.cl.ly/items/null/screenshot.png",
    "rich_thumbnail_url": "https://null.cloudfront.net/production/t/null",
    "share_url": "http://i.domain.dev/null",
    "slug": "abcdefghijk",
    "source": "python-requests/2.22.0",
    "thumbnail_url": "https://null.cloudfront.net/production/t/abcdefghijk/h200",
    "updated_at": "2019-08-18T05:26:27Z",
    "view_counter": 0
  },
  "status": true
}
  ```  

> ### add auth key
 - `HTTP method`  
  using HTTP `POST` with `form-data`

 - `tdc` (str)
  set in config.cfg
 
 - `name` (str)
  set for auth key name

 - `auth` (str)  
  set for auth key, generate from bitwarden, lastpass, 1password are recommanded.

 #### example
 ```shell
 $ curl -X POST \
  https://i.domain.dev \
  -F tdc=abcdefghijk \
  -F name=user1 \
  -F auth=abcdefghijk
 > {
  "result": "added.",
  "status": true
}
```