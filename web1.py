from flask import Flask, request, send_from_directory, url_for, render_template, jsonify, abort
import time
import random

app = Flask(__name__, static_url_path='')


def default_dash_server():
    return {
        'identifier': 'dasher',
        'version': 1,
        'desc': 'Dasher Supported Python Server v0.1',
        'data_sources': [
            {
                'id': 'ds1',
                'name': 'random data 1',
                'description': 'This is a random data for testing purposes',
                'has_live_data': True,
                'initial_data_endpoint': '/chart1init',
                'live_data_endpoint': '/chart1live'
            },
            {
                'id': 'ds2',
                'name': 'random data 2',
                'description': 'Just another random data for testing purposes',
                'has_live_data': True,
                'initial_data_endpoint': '/chart2init',
                'live_data_endpoint': '/chart2live'
            },
            {
                'id': 'ds3',
                'name': 'temperature data',
                'description': 'And another...',
                'has_live_data': False,
                'live_data_endpoint': None,
                'initial_data_endpoint': '/tempinit'
            }
        ],
        'charts': [
            {
                'id': 'ch1',
                'name': 'chart1',
                'data_source': 'ds1',
                'initial_data_endpoint': '/chart1init',
                'live_data_endpoint': '/chart1live',
                'live_update': True,
                'panel_param': {
                    'position': {
                        'left': 50,
                        'top': 80
                    },
                    'panelSize': {
                        'width': 400,
                        'height': 600
                    },
                },
                'chart_param': {
                    'chart': {
                        'renderTo': 'container2',
                        'defaultSeriesType': 'spline',
                        'events': {
                            'load': 'function'
                        }
                    },
                    'title': {
                        'text': 'Live random data'
                    },
                    'xAxis': {
                        'type': 'datetime',
                        'tickPixelInterval': 150,
                        'maxZoom': 20 * 1000
                    },
                    'yAxis': {
                        'minPadding': 0.2,
                        'maxPadding': 0.2,
                        'title': {
                            'text': 'Value',
                            'margin': 10
                        }
                    },
                    'series': [{
                        'name': 'Random data',
                        'data': []
                    }]
                }
            },
            {
                'id': 'ch2',
                'name': 'chart2',
                'data_source': 'ds2',
                'initial_data_endpoint': '/chart2init',
                'live_data_endpoint': '/chart2live',
                'live_update': True,
                'panel_param': {
                    'position': {
                        'left': 500,
                        'top': 80
                    },
                    'panelSize': {
                        'width': 400,
                        'height': 400
                    },
                },
                'chart_param': {
                    'chart': {
                        'renderTo': 'container2',
                        'defaultSeriesType': 'spline',
                        'events': {
                            'load': 'function'
                        }
                    },
                    'title': {
                        'text': 'Live random data 2'
                    },
                    'xAxis': {
                        'type': 'datetime',
                        'tickPixelInterval': 150,
                        'maxZoom': 20 * 1000
                    },
                    'yAxis': {
                        'minPadding': 0.2,
                        'maxPadding': 0.2,
                        'title': {
                            'text': 'Value',
                            'margin': 10
                        }
                    },
                    'series': [{
                        'name': 'Random data',
                        'data': []
                    }]
                }
            },
            {
                'id': 'ch3',
                'name': 'chart3',
                'data_source': 'ds3',
                'initial_data_endpoint': '/chart2init',
                'live_data_endpoint': '/chart2live',
                'live_update': True,
                'panel_param': {
                    'position': {
                        'left': 950,
                        'top': 80
                    },
                    'panelSize': {
                        'width': 400,
                        'height': 400
                    },
                },
                'chart_param': {
                    "chart": {
                        "type": "line",
                        "polar": False,
                        'events': {
                            'load': 'function'
                        }
                    },

                    "title": {
                        "text": "3RD"
                    },
                    "subtitle": {
                        "text": "3RD - - Chart"
                    },
                    "exporting": {},
                    "yAxis": [
                        {}
                    ],
                    "xAxis": [
                        {}
                    ],
                    'series': [{
                        'name': 'Serie name here',
                        'data': []
                    }],
                    'plotOptions': {
                        'series': {
                            'dataLabels': {
                                'enabled': True
                            },
                            'animation': True
                        }
                    },
                }
            }
        ]
    }


dasher_server = default_dash_server()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/profile/<profile_name>')
def profile(profile_name):
    return render_template('profile.html', profile_name=profile_name)


@app.route('/chart1init')
def chart1_init():
    timestamp = int(time.time()) * 1000 - 10000
    point_list = []
    for i in range(10):
        point_list.append([timestamp + i * 1000, random.randrange(50, 100)])

    response = {'result': point_list}
    return jsonify(response)


@app.route('/chart1live')
def chart1_live():
    timestamp = int(time.time()) * 1000
    random_number = random.randrange(50, 100)

    response = {'result': [timestamp, random_number]}
    return jsonify(response)


@app.route('/chart2init')
def chart2_init():
    timestamp = int(time.time()) * 1000 - 10000
    point_list = []
    for i in range(10):
        point_list.append([timestamp + i * 1000, random.randrange(50, 100)])

    response = {'result': point_list}

    return jsonify(response)


@app.route('/chart2live')
def chart2_live():
    timestamp = int(time.time()) * 1000
    random_number = random.randrange(50, 100)

    response = {'result': [timestamp, random_number]}
    return jsonify(response)


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about/')
@app.route('/about/<who>')
def about(who=None):
    if who is not None:
        return 'The about page of %s' % who
    else:
        return 'The PUBLIC about page'


@app.route('/editor')
def editor():
    return render_template('editor.html')


@app.route('/editor2')
def editor2():
    return render_template('highedit.html')


@app.route('/dummy')
def dummy():
    return render_template('dummy.html')


def save_chart_layout(layout_list):
    global dasher_server
    for layout in layout_list:
        chart_id = layout['id']
        # print(chartId)

        new_chart_param = {
            'position': layout['position'],
            'panelSize': layout['size']
        }
        # print(new_chart_param)

        for chartItem in dasher_server['charts']:
            # print(chartItem['id'])
            if chartItem['id'] == chart_id:
                chartItem.update({'panel_param': new_chart_param})


def delete_chart(chart_id):
    global dasher_server
    dasher_server['charts'] = [chart for chart in dasher_server['charts'] if chart['id'] != chart_id]


@app.route('/dasher', methods=['GET', 'POST', 'PUT'])
def dasher():
    global dasher_server
    if request.method == 'GET':
        return jsonify(dasher_server)
    elif request.method == 'POST':
        if request.json:
            # print(request.json)
            # ========= POST ==============
            if request.json['op'] == 'insert':
                insert_chart(request.json['data'])
                return jsonify({'success': True, 'message': 'ok'})

            elif request.json['op'] == 'saveLayout':
                save_chart_layout(request.json['data'])
                return jsonify({'success': True, 'message': 'chart layout saved'})

            elif request.json['op'] == 'deleteChart':
                delete_chart(request.json['data'])
                return jsonify({'success': True, 'message': 'chart removed'})

            elif request.json['op'] == 'reset':
                dasher_server = default_dash_server()
                return jsonify({'success': True, 'message': 'chart reset'})

            else:
                return jsonify({'success': False, 'message': 'invalid op parameter!'})

        elif request.form:
            return jsonify(
                {'success': False, 'message': 'You need to send the POST data as application/json, not as form'})
        else:
            return jsonify({'success': False, 'message': 'bad request!'})

            #
            # elif (request.form['op'] == 'insert'):
            #     insert_chart(request.json['data'])
            #     return jsonify({'success':True, 'message':''})
            # else:
            #     return jsonify({'success':False, 'message': 'bad bad request'})


@app.route('/addchart')
def add_chart():
    return render_template('addchart.html')


@app.route('/postdene', methods=['POST'])
def post_dene():
    param1 = request.json
    return jsonify(param1)


def insert_chart(chart_info):
    dasher_server['charts'].append(chart_info)


if __name__ == "__main__":
    app.run(debug=True)
