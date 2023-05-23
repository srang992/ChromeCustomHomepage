hot_reload:
	flet run main.py -a assets -d

create_dist:
	flet publish main.py --assets assets

run_dist:
	python -m http.server --directory dist