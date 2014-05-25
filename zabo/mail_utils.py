# -*- coding: utf-8 -*-


def mailbody_transfer_directions(new_abo):
    if new_abo.locale == 'de':
        body_lines = u'''Hallo ''' + new_abo.name + u''' !

Wir haben die Daten zu Deinem regelmäßigen Unterstützungsbeitrag erhalten.

Bitte richte nun einen monatlichen Dauerauftrag über den folgenden, von Dir
gewählten Betrag ein: ''' + new_abo.amount + u''' €

Die Zahlung sollte auf unser Konto bei der Ethikbank eingehen:

EthikBank eG
Kontoinhaber: C3S SCE
BIC:\t GENO DE F1 ETK
IBAN:\t DE79830944950003264378

Betrag (€): ''' + str(new_abo.amount) + u'''
Verwendungszweck: ''' + new_abo.refcode + u'''

Bitte achte darauf den Verwendungszweck exakt zu übernehmen,
damit wir Dir die Zahlung eindeutig zuordnen können.

Sobald wir den Eingang der Zahlung bestätigen können, schicken wir Dir eine
E-Mail mit den Grafik-Links zum Einbinden des Banners im Netz für die Anzeige
auf z.B. einer Website und einen Link zu Deiner persönlichen Beitrags-Status-
Seite, die dein Engagement bestätigt.


Bis bald!

Dein C3S-Team
'''
    else:
        body_lines = u'''Hello ''' + new_abo.name + u''',

we have received your details on your regular contribution.

Please set up a monthly standing order for the following amount you have
selected: ''' + str(new_abo.amount) + u''' €

The payment shall be made to our account at the EthikBank:

EthikBank eG
Account holder: C3S SCE
BIC:\t GENO DE F1 ETK
IBAN:\t DE79830944950003264378

Amount (€): ''' + str(new_abo.amount) + u'''
Intended use: ''' + new_abo.refcode + u'''

Please make sure to copy the intended use accurately so that we can correctly
assign your payment.

As soon as we can confirm the receipt of payment, we will send you an e-mail
with a link to your banner, which you may implement online, for example on a
website, and a link to your personal page of your contribution status,
confirming your commitment.

Many thanks for your support! Until soon
Your C3S team
'''
    return body_lines

#############################################################################


def mailbody_transfer_received(_abo, _url):
    '''
    this function is used by the 'send_mail_view' view in backend_views.py
    i.e. confirm paymant and send out links.

    depending on a datasets locale setting, language is chosen
    '''
    if _abo.locale == 'de':
        body_lines = u'''Hallo {},

Wir haben Deine Überweisung erhalten. Dankeschön!

Du kannst folgenden Link benutzen, um Deine Grafik zu laden,
und auf Deiner Website zu hosten:

  {}/sponsor/{}.png

Du kannst auf die folgende Seite verlinken,
die öffentlich (!) den aktuellen Status deines Abos anzeigt:

  {}/sponsor/{}.html

Bis bald!

Dein C3S-Team
    '''.format(_abo.name, _url, _abo.linkcode, _url, _abo.linkcode,)

    else:  # default fallback: english
        body_lines = u'''Hello {},

we have received your payment. Thank you very much!

You may use the following link to download your banner
for hosting it on your website:

  {}/sponsor/{}.png

You may also link to the following page, if you want to make public (!)
the current status of your support:

  {}/sponsor/{}.html

Until soon

Your C3S team
    '''.format(_abo.name, _url, _abo.linkcode, _url, _abo.linkcode,)

    return body_lines
