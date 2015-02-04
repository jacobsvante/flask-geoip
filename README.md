**Author:** Jacob Magnusson. [Follow me on Twitter](https://twitter.com/jacobsvante_)

## About

This is a simple Flask extension for pygeoip. Not yet thoroughly tested, but has been working great for me so far.


## Installation

Install using `pip`...

    pip install Flask-GeoIP

...or clone the project from github.

    git clone https://github.com/jmagnusson/Flask-GeoIP.git


## Configuration


The GeoIP file that you want to use needs to be set in your config:

    GEOIP_FILEPATH = '/path/to/geoip.dat'

You can change the caching method (default is 'STANDARD') that is used
by pygeoip:

    GEOIP_CACHE = 'MEMORY_CACHE'

Then in the code you do:

    from flask.ext.geoip import GeoIP
    app = Flask(__name__)
    app.config.from_pyfile('/path/to/myconfig.py')
    geoip = GeoIP(app)
    country = geoip.country_name_by_addr('1.2.3.4')

Or if using a factory function for creating your app:

    from flask.ext.geoip import GeoIP
    geoip = GeoIP()
    ...
    app = create_app('/path/to/myconfig.py')
    geoip.init_app(app)
    country = geoip.country_name_by_addr('1.2.3.4')


## Documentation

This readme.


## Credits

Thanks go out to [maxmind](https://github.com/maxmind/geoip-api-c) and [appliedsec](https://github.com/appliedsec/pygeoip) for making these great libs.
