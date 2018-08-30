from django.conf import settings
from django.core.management.base import BaseCommand, CommandError
from django.template.loader import render_to_string
from os.path import join
from sekizai.context_processors import sekizai


class Command(BaseCommand):
    help = "Used to make error pages."

    requires_system_checks = False

    def handle(self, *args, **options):

        for error_page in "400.html", "403.html", "404.html", "500.html":
            try:
                content = render_to_string(error_page, context=sekizai())
                with open(join(settings.MEDIA_ROOT, error_page), "w") as out:
                    out.write(content)
            except IOError as err:
                message = "Cannot make error page: {!s}".format(err)
                raise CommandError(message) from err
