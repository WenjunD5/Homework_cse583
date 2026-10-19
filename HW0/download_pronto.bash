mkdir pronto
echo "Pronto data in 2015" > pronto/README.txt
cd pronto
mkdir data
cd data
curl -O  https://s3.amazonaws.com/pronto-data/open_data_year_one.zip
unzip open_data_year_one.zip
head 2015_trip_data.csv
