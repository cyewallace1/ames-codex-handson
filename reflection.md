# Reflection

## Where Codex struggled

Most of the trouble was with the environment, not the analysis. My file had been saved as AmesHousing-1.csv, and Codex handled that fine, but it could not find a Python with pandas. It tried the Homebrew and Xcode versions and never found my Anaconda install, even though my own terminal uses it. Its first attempt to install packages failed because it did not have network access until I approved it. Even after it set up a project environment, it kept slipping back to the system Python for its own checks. In Prompt 4 its verification failed for that reason, and the quick count it fell back on never confirmed that every neighborhood had at least 10 sales.

## What surprised me

Codex did more than I asked. In Prompt 2 it built the chart and added a .gitignore for the virtual environment before I requested either one. The .gitignore was a good call, but the chart meant I had to stop and review something I had not specified yet. It also looked up the dataset documentation on its own to confirm the 4,000 square foot cutoff instead of just taking my word for it. I was also surprised that /transcript, which the assignment tells us to use, was not recognized in my version of Codex, so I had to copy the session from the terminal myself.

## How my prompts evolved

My first prompt was broad and told Codex not to analyze yet, which gave me the column names and sales counts to work from. After that my prompts got more specific and more reactive. I used the exact column names it reported, named GrnHill and Greens when their small sample sizes skewed the rankings, and pointed out exactly what was wrong with its verification. By Prompt 5 I was asking Codex to prove its results with a worked example instead of just reporting numbers.

I also used Claude alongside Codex to help plan my prompts and to double check Codex's numbers, like the regression results and the worked residual example. Having a second tool review the output made it easier to catch problems like the weak verification in Prompt 4.

## What I would do differently

I would set up the Python environment before starting, either by pointing Codex straight to my Anaconda install or by creating the project environment myself first. A good part of the session went to getting pandas working instead of doing analysis. I would also save the transcript as I went instead of piecing it together at the end.