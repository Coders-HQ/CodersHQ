import requests
import os
class PluralSight:
    """
    Get everything related pluralsight
    """

    URL = "https://paas-api.pluralsight.com/graphql"
    AUTH = "Bearer " + os.getenv('PLURAL_TOKEN')

    @classmethod
    def all_skills(cls):
        query = """
        {
            skillAssessmentResults (first: 500) {
                nodes {
                    quintileLevel
                    measurementType
                    skillName
                }
            }
        }
        """

        request = requests.post(
            PluralSight.URL,
            headers={'Authorization': PluralSight.AUTH},
            json={'query': query}
        )

        return request.json()['data']['skillAssessmentResults']['nodes']

    @classmethod
    def get_user(cls, id):
        """
        get specific user based on portfolio id
        """

        query = """
        {
            users (filter: {
                emails: \"""" + f'{id}@codershq.ae' + """\" 
            }) {
                nodes {
                    id
                    createdOn
                }
            }
        }
        """

        request = requests.post(
            PluralSight.URL,
            headers={'Authorization': PluralSight.AUTH},
            json={'query': query}
        )

        return request.json()['data']['users']['nodes']

    @classmethod
    def get_psid(cls, id):
        """
        returns ps id
        """

        data = PluralSight.get_user(id)[0]
        return data["id"]

    @classmethod
    def get_user_skill_psid(cls, psid):
        """
        returns user skill based on pluralsight id
        """



        query = """
        {
            skillAssessmentResults (filter: {
                userIds: \"""" + psid + """\" 
            }) {
                nodes {
                    quintileLevel
                    measurementType
                    skillName
                }
            }
        }
        """

        request = requests.post(
            PluralSight.URL,
            headers={'Authorization': PluralSight.AUTH},
            json={'query': query}
        )

        return request.json()['data']['skillAssessmentResults']['nodes']


    @classmethod
    def get_user_skill(cls, id):
        psid = PluralSight.get_psid(id)
        return PluralSight.get_user_skill_psid(psid)