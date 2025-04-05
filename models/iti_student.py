from odoo import models, fields, api

class ITIStudent(models.Model):
    _name = "iti.student"

    _rec_name = "age"

    name = fields.Char()
    age = fields.Integer()
    info = fields.Text()
    is_accepted = fields.Boolean()
    birth_date = fields.Date()
    image = fields.Binary()
    gender = fields.Selection([('Male','m'),('Female','f')])

    salary = fields.Float("")
    is_working = fields.Boolean("")
    cv = fields.Html()
    track_id = fields.Many2one("iti.track")
    track_capacity = fields.Integer(related="track_id.capacity")


    @api.onchange('is_working')
    def change_work_state(self):
        self.is_accepted = True
        return {
            'warning': {
                'title': ('state changed'),
                'message': 'working state is changed to %s'%(self.is_working)
            }
        }

    def approve_action(self):
        print("state changed")
        self.salary = 20000
