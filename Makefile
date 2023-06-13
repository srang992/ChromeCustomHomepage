hot_reload:
	flet run main.py -a assets -d

create_dist:
	flet publish main.py --assets assets

run_dist:
	python -m http.server 8500 --directory dist

docker_img:
	docker build --tag my-homepage-img .

docker_container:
	docker run --name MyHomepage -p 3000:8500 my-homepage-img