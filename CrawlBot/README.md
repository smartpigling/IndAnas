#run mongo
docker run --name scrapy-mongo -p 27017:27017 -v /DataFiles:/data/db -d mongo:latest

#run splash
docker run -p 8050:8050 -p 5023:5023 -d scrapinghub/splash

#start 
scrapy crawl bot_name
