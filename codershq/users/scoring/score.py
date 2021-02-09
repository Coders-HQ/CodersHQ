from github import Github
import concurrent.futures


class CHQScore:

    def __init__(self, auth=None):

        self.auth = auth
        if auth is not None:
            self.g = Github(auth)
        else:
            self.g = Github()

    def check_user_exists(self, user_name):
        """
        Tries to get user info, returns true if
        call succeeds, else, false
        """
        try:
            user = self.g.get_user(user_name)
            return True
        except:
            return False

    def get_scores(self, user_list):
        """
        Returns a dict of username and associated score
        """
        
        score_dict = {}
        def download(user_name):
            score_dict[user_name]=self.get_score(user_name)

        # thread all calls
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
            futures = []
            for user in user_list:
                futures.append(executor.submit(download, user))
            for future in concurrent.futures.as_completed(futures):
                print(future.result())

        return score_dict

    def get_score(self, user_name):
        """
        Gets github API score
        """

        # user data
        user = self.g.get_user(user_name)

        # modifiers

        # class modifiers
        m_high = 3
        m_med = 2
        m_low = 1

        # user modifiers
        m_u_public_repos = 2
        m_u_created_at = 3
        m_u_public_gists = 3
        m_u_followers = 1

        # repo modifiers
        m_r_created_at = 1
        m_r_stargazers_count = 2
        m_r_watchers_count = 2
        m_r_forks_count = 3
        m_r_subscribers_count = 2
        m_r_open_issues_count = 1
        m_r_has_projects = 1
        m_r_has_wiki = 1

        # commit modifiers
        m_c_commits = 1

        # ================== SCORE ===================

        user_score = 0
        repo_score = 0
        commit_score = 0

        user_score += user.public_repos * m_u_public_repos
        user_score += user.public_gists * m_u_public_gists
        user_score += user.followers * m_u_followers

        # per repo
        current_user_id = user.id

        for repo in user.get_repos():

            if not repo.fork:
                current_repo_score = 0
                current_repo_score += repo.stargazers_count * m_r_stargazers_count
                current_repo_score += repo.watchers_count * m_r_watchers_count
                current_repo_score += repo.forks_count * m_r_forks_count
                current_repo_score += repo.subscribers_count * m_r_subscribers_count
                current_repo_score += repo.open_issues_count * m_r_open_issues_count
                repo_score += current_repo_score
                commit_score += repo.get_commits().totalCount * m_c_commits

        # apply modifier
        user_score *= m_high
        repo_score *= m_med
        commit_score *= m_low
        total_score = user_score+repo_score+commit_score

        return total_score


if __name__ == "__main__":
    chq_score = CHQScore()
    print(chq_score.get_score("ralsuwaidi"))
