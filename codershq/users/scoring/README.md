# CHQ_Scoring

The scoring system looks at each attribute and attaches a modifier (currently set at 1,2 and 3) for the significance of said attribute. After that another modifier is applied for the class attribute, these are then added together to get the final score. 

## Modifiers

Modifiers and and priority.

```
high [3], med [2], low [1]

user class priority:     [3] HIGH
user public repos:       [2] 6
user created at:         [3] 2011-09-03 15:26:22
user public gist:        [3] 0
user followers:          [1] 127901

Single repo example

repo class priority:     [2] MEDIUM
repo is forked:          [M] True
repo created at:         [1] 2017-01-17 00:25:49
repo stargazer count:    [2] 84
repo watchers count:     [2] 84
repo fork count:         [3] 33
repo sub count:          [2] 9
repo open issues:        [1] 0
repo has projects:       [M] True
repo has wiki:           [M] True

single repo commits example

commit class priority:   [1] LOW
commits count:           [1] 1691
```

## Initial calculation

The calculation has some limitations and does not take into account who created the commits.

[repo under construction]