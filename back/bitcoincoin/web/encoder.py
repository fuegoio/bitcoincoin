import datetime
import json
import pendulum


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            date = pendulum.instance(obj)
            return {'str': str(date), 'diff': date.diff_for_humans(locale='fr')}
        elif isinstance(obj, datetime.date):
            date = pendulum.instance(datetime.datetime(obj.year, obj.month, obj.day))
            return {'str': str(date), 'diff': date.diff_for_humans(locale='fr')}
        else:
            return super().default(obj)
