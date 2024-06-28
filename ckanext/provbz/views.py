import logging

# For CKAN 2.10
from ckan.common import CKANConfig as config
from flask import Blueprint
from ckan.plugins.toolkit import render

log = logging.getLogger(__name__)

blueprints = Blueprint('blueprints', __name__)

# Define the views
@blueprints.route('/about')
def provbzinfo():
    return render('home/info.html')

@blueprints.route('/faq')
def provbzfaq():
    return render('home/faq.html')

@blueprints.route('/privacy')
def provbzprivacy():
    return render('home/privacy.html')

@blueprints.route('/legal')
def provbzlegal():
    return render('home/legal.html')

@blueprints.route('/acknowledgements')
def rovbzacknowledgements():
    return render('home/acknowledgements.html')

@blueprints.route('/formats')
def provbzformats():
    return render('home/formats.html')


def get_blueprints():
    return [blueprints]