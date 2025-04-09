from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class ITIStudent(models.Model):
    _name = "iti.student"

    _rec_name = "age"

    name = fields.Char()
    age = fields.Integer(compute="compute_age", store=True)
    graduate_age =fields.Integer(compute="compute_age")
    birth_date = fields.Date()
    info = fields.Text()
    is_accepted = fields.Boolean()
    image = fields.Binary()
    gender = fields.Selection([('Male','m'),('Female','f')])
    salary = fields.Float("")
    is_working = fields.Boolean("")
    cv = fields.Html()
    track_id = fields.Many2one("iti.track")
    track_capacity = fields.Integer(related="track_id.capacity")

    level = fields.Selection([('level1','Level1'),('level2','Level2'),('level3','Level3')])

    level_logs = fields.One2many('iti.student.log','student_id')

    roll_id = fields.Integer()

    _sql_constraints = [('unique_roll_id','UNIQUE(roll_id)',"Roll Id can't be duplicate for each student" )]




    # @api.onchange('is_working')
    # def change_work_state(self):
    #     self.is_accepted = True
    #     return {
    #         'warning': {
    #             'title': ('state changed'),
    #             'message': 'working state is changed to %s'%(self.is_working)
    #         }
    #     }

    def approve_action(self):
        print("state changed")
        self.salary = 20000
        self.level = "level3"


    def create_level_log(self):
        vals = {
            'description': "Level changed to %s"%(self.level),
            'student_id':self.id
        }
        self.env['iti.student.log'].create(vals)

    @api.constrains('age')
    def check_age(self):
        if self.age < 0:
            raise ValidationError("Age can't be negative number")
        elif self.age == 0:
            raise ValidationError("Age can't be zero")

    @api.constrains('is_working','salary')
    def check_salary(self):
        if self.is_working == True:
            if self.salary < 10000:
                raise ValidationError("Salary can't be less than 10000")

    @api.depends('age','graduate_age','birth_date')
    def compute_age(self):
        for rec in self:
            if rec.birth_date:
                today = date.today()
                rec.age = today.year - rec.birth_date.year - (
                        (today.month, today.day) < (rec.birth_date.month, rec.birth_date.day)
                )
                rec.graduate_age = rec.age + 5
                print(f"Computed age for {rec.name}: {rec.age}")
            else:
                rec.age = 0
                rec.graduate_age = rec.age + 5





