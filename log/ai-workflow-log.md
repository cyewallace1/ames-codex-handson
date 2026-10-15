# AI Workflow Log

## Prompt 1, October 15, 2026, 5:35 PM
**Asked for** folders plus a first look at the data before any analysis
**Codex produced** It created the analysis, prompts, and log folders and reported 2,930 rows and 82 columns, the column names SalePrice, Gr Liv Area, and Neighborhood, zero missing values in those three columns, and the number of sales in each neighborhood. It also found that my file had been saved as AmesHousing-1.csv and that pandas was not installed, so it used Python's built in csv module instead.
**Accepted** The folders, the column names, and the sales counts. The neighborhood counts added up to the 2,930 total rows.
**Modified** Nothing in this step.
**Rejected** Relying on the csv module going forward, since the regression and chart needed pandas and matplotlib.
**Why** I told Codex not to analyze yet so I could confirm the column names and catch data problems first. The counts showed that GrnHill, Greens, and Landmrk had very few sales, which mattered later.

## Prompt 2, October 15, 2026, 5:55 PM
**Asked for** renaming the file, getting pandas working, and the regression with the neighborhood table
**Codex produced** It renamed the file to AmesHousing.csv and searched for a Python with pandas. It tried the Homebrew and Xcode versions and never found my Anaconda install. It created a virtual environment in analysis/.venv, and its first install failed because it did not have network access. After I approved the install it wrote analysis/neighborhood_value.py, saved the neighborhood table, and printed a slope of 111.69, an intercept of 13,290, and an R squared of 0.50. It also made a chart and a .gitignore that I had not asked for yet.
**Accepted** The rename, the install into the project environment, the script, and the regression results. The slope and R squared lined up with what is usually reported for the full Ames dataset. I kept the .gitignore because it stops the virtual environment from being committed to my repo.
**Modified** Nothing in the code.
**Rejected** Nothing outright, but I did not accept the chart until I had reviewed it.
**Why** Approving the install was the quickest fix since the assignment does not require a specific Python. I held off on the chart because Codex made it before I had said what I wanted from it.

## Prompt 3, October 15, 2026, 5:59 PM
**Asked for** fixes to the chart it made on its own and a look at both ends of the table
**Codex produced** It sorted the bars from highest to lowest, colored neighborhoods above prediction blue and below prediction red, and formatted the axis in dollars. It reran the script and showed the first and last five rows of the table.
**Accepted** The updated chart after I previewed the image myself, and the table. The average prices made sense, with StoneBr and NridgHt the most expensive and MeadowV and IDOTRR the cheapest.
**Modified** Nothing in this step.
**Rejected** Nothing, but I flagged a problem with the results.
**Why** The top five included GrnHill with only 2 sales and Greens with 8. Averages based on that few houses are not reliable, so I decided to filter out small neighborhoods next.

## Prompt 4, October 15, 2026, 6:04 PM
**Asked for** dropping neighborhoods under 10 sales and removing houses over 4,000 square feet
**Codex produced** It searched the web and found the dataset documentation by De Cock (2011) supporting the 4,000 square foot cutoff. It removed 5 houses over that size, kept small neighborhoods in the regression but left them out of the table and chart, and reran. The slope rose from 111.69 to 116.23 and R squared from 0.50 to 0.52. StoneBr became the top neighborhood and SWISU stayed at the bottom.
**Accepted** Removing the outliers, since Codex backed it up with the documentation, and the new results. Taking out the 5 very large houses made sense because they were pulling the regression line down.
**Modified** Nothing in the code.
**Rejected** Its verification. It ran the check with the system Python instead of the project environment, so the pandas command failed and it fell back to a quick csv count of the rows. That count never confirmed that every remaining neighborhood had at least 10 sales.
**Why** A check that does not test the thing I asked for does not prove it worked, so I asked Codex to verify the output properly in the next prompt.

## Prompt 5, October 15, 2026, 6:07 PM
**Asked for** a proper check of the output file and one worked residual example
**Codex produced** Using the project environment, it confirmed the table has 25 neighborhoods and every one has at least 10 sales. It listed the top three (StoneBr, NridgHt, Timber) and bottom three (IDOTRR, OldTown, SWISU) with their sales counts and walked through house #1 in NAmes. With 1,656 square feet and a sale price of $215,000, the model predicted $199,243, so the house sold $15,757 above prediction.
**Accepted** All of it. The arithmetic checked out when I verified it.
**Modified** Nothing.
**Rejected** Nothing.
**Why** Seeing one real house worked through step by step confirmed the residuals mean what I thought. I also noticed the intercept had changed to $6,773 after filtering, which Codex had not mentioned in Prompt 4.

## Prompt 6, October 15, 2026, 6:08 PM
**Asked for** the README with my question, date, summary, and file list
**Codex produced** It wrote README.md with my question, the session date of October 15, 2026, a plain language summary of the final filtered results that covers both cleaning steps, and a short description of each file in the analysis folder.
**Accepted** The README. I checked that its numbers matched the final output, with StoneBr at $90,907.59, SWISU at negative $61,901.78, a slope of 116.23, and an R squared of 0.52.
**Modified** Nothing in the README. Afterward I kept matplotlib's font cache folder out of my commit, and I saved the session transcript myself because /transcript was not recognized in my version of Codex.
**Rejected** Nothing.
**Why** The summary was accurate and in plain language, which is what the assignment asked for.