build:
	python setup.py py2app --alias

clean:
	rm -rf ./build/ ./dist/

install: clean
	python setup.py py2app
