from odoo import models, fields, api, SUPERUSER_ID

class BannerCompany(models.Model):
    _inherit = 'res.company'
    banner = fields.Binary('Bild auf EZ QR', help="Bild, das auf dem QR Einzahlungsschein angezeigt werden soll.")