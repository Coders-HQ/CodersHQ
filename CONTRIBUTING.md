# How to contribute with Git and GitHub best practices

Creating effective pull requests and commit messages is essential for collaborative software development.

The **rule of thumb** is simple — collaboration is a process provided by humans for humans, so treat your fellow contributors with all respect and don't forget to add a bit of love on top of every piece of your work.

By following these best practices, you can ensure that your contributions are clear, concise, and easy to understand, making it easier for others in your team to review and collaborate on your code.

## Branch naming strategy

The **branch name** is your first opportunity to give your task context.

It is recommended to combine [**Github issues**](https://github.com/Coders-HQ/CodersHQ/issues) with a short description that describes the task resolved in this branch, for example: `Coders-HQ-portfolio/challenge-form` or `Coders-HQ-eventbrite/adding-api`.

If you don't have Github issue for you PR, then you may avoid the prefix, but keep in mind that more likely you have to create the issue first. 

## Commit your changes

Write a descriptive **summary**: The first line of your commit message should be a concise summary of the changes you are making. It should be no more than 50 characters and should describe the change in a way that is easy to understand.

Provide more **details** in the body: The body of the commit message should provide more details about the changes you are making. Explain the problem you are solving, the changes you are making, and the reasoning behind those changes.

Use the **commit history** in your favor: Small and self-contained commits allow the reviewer to see exactly how you solved the problem. By reading the commit history of the PR, the reviewer can already understand what they'll be reviewing, even before seeing a single line of code.

## Create a pull request

The **title** of your pull request should be clear and descriptive. It should summarize the changes you are making in a concise manner.

Provide a detailed **description** of the changes you are making. Explain the reasoning behind the changes, the problem it solves, and the impact it may have on the codebase. Keep in mind that a reviewer was not working on your task, so you should explain why you wrote the code the way you did.

Describe the scene and provide everything that will help to understand background and a context for the reviewers by adding related Github issues to the description, links to the related PRs, project or third-party documentation. If there are any potential drawbacks or trade-offs to your changes, be sure to mention them too.

Be sure to **request reviews** from the appropriate people. This might include the project maintainers, other contributors, or anyone else who is familiar with the codebase and can provide valuable feedback.

## Getting a better review

**Draft pull requests** in allow you to create a pull request that is still a work in progress and not ready for review. This is useful when you want to share your changes with others but aren't quite ready to merge them or request immediate feedback.    
https://github.blog/2019-02-14-introducing-draft-pull-requests/

Once your pull request has been reviewed, be sure to **respond** to any feedback you receive. This might involve making additional changes to your code, addressing questions or concerns, or simply thanking reviewers for their feedback.  

By using the **re-request review** feature, you can prompt the reviewer to take another look at your changes and provide feedback if necessary.  
https://github.blog/changelog/2019-02-21-re-request-review-on-a-pull-request/

The **CODEOWNERS** file in GitHub allows you to specify who is responsible for code in a specific part of your repository. You can use this file to automatically assign pull requests to the appropriate people or teams, and to ensure that the right people are notified when changes are made to certain files or directories.  
https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
 
We use **scheduled reminders** to Slack for abandoned pull requests to will receive reminders to the team's channel for PRs that are non-draft and have no activity for a couple of days.
https://docs.github.com/en/organizations/organizing-members-into-teams/managing-scheduled-reminders-for-your-team

## Finalize the change

We are actively using **threads** to allow for more detailed and targeted discussions about specific parts of the pull request.  Resolved thread means that the conversation has been addressed and the issue has been resolved. Reviewers are responsible on resolving the comment and not the author. The author can simply add a reply comment that the change has been done or decline a request.

When your pull request is approved, be sure to **merge it responsibly**. This might involve running additional tests or checks, ensuring that the codebase is still functional.

### For curious minds

- How to write a Git commit message:  
https://cbea.ms/git-commit/

- 13 tips to make your PR easier to review:  
https://blog.codacy.com/13-tips-to-make-your-pr-easier-to-review/

Happy contributing!
