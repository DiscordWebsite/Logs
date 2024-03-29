import re

from rest_framework.routers import DefaultRouter


class OptionalSlashRouter(DefaultRouter):
    def __init__(self, *args, **kwargs):
        super(DefaultRouter, self).__init__(*args, **kwargs)
        self.trailing_slash = '/?'


rowboat_re = r'(?P<timestamp>(?:[\d-]+) (?:[\d:.]+)) \((?P<message_id>[\d]{16,19}) \/ (?P<guild_id>[\d]{16,19}) \/ ' \
             r'(?P<user_id>[\d]{16,19})\) (?P<username>.*?)#(?P<discriminator>\d{4}|\d): (?P<content>[\S\s]*?)? \(' \
             r'(?P<attachments>(?:http(?:|s):.*))?\)$'

rosalina_bottings_re = r'(?P<timestamp>(?:[\d-]{10})T(?:[\d:.]{8,15}))(?:\+[\d:]{5}|Z) \| (?P<guild_name>.*?)\[(?P' \
                       r'<guild_id>\d{16,19})\] \|  (?P<channel_name>[\w-]{1,100})\[(?P<channel_id>\d{16,19})\] \| ' \
                       r'(?P<username>.*?)\[(?P<user_id>\d{16,19})\] \| said: (?P<content>[\S\s]*?)(?:\nAttachment: ' \
                       r'(?P<attachments>(?:http(?:|s):.*)))?\nMessage ID: (?P<message_id>\d{16,19})$'

auttaja_re = r'\[(?P<timestamp>[\w :]{24,25})\] \((?P<username>.*?)#(?P<discriminator>\d{4}|\d) - (?P<user_id>\d{16,19' \
             r'})\) \[(?P<message_id>\d{16,19})\]: (?P<content>[\S\s]*?)(?: (?P<attachments>(?:http(?:|s):.*))?)?$'

gearbot_re = r'(?P<timestamp>[\w\-. :]{26}) (?P<guild_id>\d{16,19}) - (?P<channel_id>\d{16,19}) - (?P<message_id' \
             r'>\d{16,19}) \| (?P<username>.*?)#(?P<discriminator>\d{4}|\d) \((?P<user_id>\d{16,19})\) \| (?P<content>' \
             r'[\S\s]*?)? \|(?: ?(?P<attachments>(?:http(?:|s):.*))?)?$'

modmailbot_re = r'\[(?P<timestamp>[\d :-]{19})\](?:(?: \[(?:(?:(?:FROM|TO) USER)|CHAT|COMMAND)\]) \[(?P<username>.*?)' \
                r'(?:#(?P<discriminator>\d{4}|\d))?\]( \(Anonymous\) [^:]+?:)? (?P<content>[\S\s]*?)(?:\n{2}\*\*' \
                r'Attachment:\*\* (?P<attachments>(?:http(?:|s):.*)))?$| (?P<bot_content>[^\n]+))'

vortex_re = r'\[(?P<timestamp>[\w, :]{28,29})\] (?P<username>.*?)#(?P<discriminator>\d{4}|\d) \((?P<user_id>\d{16,19})' \
            r'\) : (?P<content>[\S\s]*?)(?P<attachments>(?:\n(?:http(?:|s):.*)|)*?)$'

yggdrasil_re = r'\[Author ID: (?P<user_id>\d{16,19}) \| Message ID: (?P<message_id>\d{16,19})\] (?:<=|=>) ' \
               r'(?P<username>.*?)#(?P<discriminator>\d{4}|\d) : (?P<content>[\S\s]*?)?$'


_private_types = {
    'giraffeduck': 'GiraffeDuck',
    'logger': 'Logger',
    'throttle-bot': 'Throttle-Bot',
    'scheggia': 'Scheggia Services',
    'melanie': 'Melanie',
}


_public_types = {
    'auttaja': 'Auttaja',
    'gearbot': 'Gearbot',
    'modmailbot': 'ModMailBot',
    'rosalina_bottings': 'Rosalina Bottings',
    'rowboat': 'Rowboat',
    'vortex': 'Vortex',
    'yggdrasil': 'Yggdrasil',
}


rowboat_types = {
    'aperture': 'Aperture',
    'heimdallr': 'Heimdallr',
    'jetski': 'Jetski',
    'lmg_showboat': 'LMG Showboat',
    'rawgoat': 'Rawgoat',
}

all_types = {**_public_types, **_private_types, **rowboat_types}

form_types = {k: all_types[k] for k in sorted({**_public_types, **rowboat_types})}

expiry_times = {
    '10min': 60 * 10,
    '30min': 60 * 30,
    '1hour': 60 * 60,
    '1day': 60 * 60 * 24,
    '1week': 60 * 60 * 24 * 7,
    '2weeks': 60 * 60 * 24 * 14,
    '1month': 60 * 60 * 24 * 30,
    '1year': 60 * 60 * 24 * 365,
    'never': None
}

form_expiry_times = list((k, re.sub(r'(\d+|)(\w+)', lambda m: (m.group(1) + ' ' if m.group(1) else ''
                                                               ) + m.group(2).title(), k)) for k in expiry_times)

form_privacy_types = [
    ('public', 'Public'),
    ('guild', 'Guild Only'),
    ('mods', 'Mods Only')
]

privacy_types = [p[0] for p in form_privacy_types]


task_messages = [
    '{current}/{total} messages parsed... ({percent}%)',
    '{current}/{total} messages formatted... ({percent}%)',
    'Saving messages... ({percent}%)'
]
