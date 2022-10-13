
from codershq.api.utils.pluralsight import PluralSight
from codershq.portfolio.models import Portfolio


class Analytics:

    def __init__(self):
        self.all_skills = PluralSight.all_skills()

    def total_skills(self):
        """
        return total skills
        """
        return len(self.all_skills)

    def total_profiles(self):
        """
        return number of profiles
        """
        return len(Portfolio.objects.filter())

    def quintile_levels(self):
        """
        return quintile levels as row

        eg: [5,5,5,6,3]

        which means 5 novice, etc 
        """
        quintile_levels = []
        novice = 0
        proficient_emerging = 0
        proficient_average = 0
        proficient_above_average = 0
        expert = 0
        for skill in self.all_skills:
            quintile = skill['quintileLevel']
            if quintile == 'novice':
                novice += 1
            elif quintile == 'proficient-emerging':
                proficient_emerging += 1
            elif quintile == 'proficient-average':
                proficient_average += 1
            elif quintile == 'proficient-above-average':
                proficient_above_average += 1
            elif quintile == 'expert':
                expert += 1

        quintile_levels = [novice,
                           proficient_emerging,
                           proficient_average,
                           proficient_above_average,
                           expert]

        return quintile_levels

    def repeat_num(self):
        """
        return total number of repeats
        """
        retakes = [x for x in self.all_skills if x['measurementType'] == 'retake']
        return len(retakes)

    def local_num(self):
        """
        return number of locals
        """

        return Portfolio.objects.filter(nationality='AE').count()

    def total_males(self):
        """
        return total males
        """

        return Portfolio.objects.filter(gender='M').count()

    def total_local_males(self):
        """
        return total males
        """

        return Portfolio.objects.filter(gender='M', nationality='AE').count()

    def total_female(self):
        """
        return total female
        """

        return Portfolio.objects.filter(gender='F').count()

    def total_local_female(self):
        """
        return total female
        """

        return Portfolio.objects.filter(gender='F', nationality='AE').count()

    def looking_for_jobs(self):
        """
        return number of people looking for jobs
        """
        return Portfolio.objects.filter(is_seeking_job=True).count()

    def json(self):
        """
        return full data as a dict 
        """
        data = {
            "total_skill": self.total_skills(),
            "total_profiles": self.total_profiles(),
            "quintile_levels": self.quintile_levels(),
            "repeat_num": self.repeat_num(),
            "local_num": self.local_num(),
            "total_males": self.total_males(),
            "total_local_males": self.total_local_males(),
            "total_female": self.total_female(),
            "total_local_female": self.total_local_female(),
            "looking_for_jobs": self.looking_for_jobs(),
        }

        return data
