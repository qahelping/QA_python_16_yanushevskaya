from visual_regression_tracker import VisualRegressionTracker, Config, TestRun

config = Config(
    # apiUrl - URL where backend is running
    apiUrl="http://localhost:4200",
    # project - Project name or ID
    project="Default project",
    # apiKey - User apiKey
    apiKey="tXZVHX0EA4YQM1MGDD",
    # ciBuildId - Current git commit SHA
    ciBuildId="commit_sha",
    # branch - Current git branch
    branchName="develop",
    # enableSoftAssert - Log errors instead of exceptions
    enableSoftAssert=False,
)

vrt = VisualRegressionTracker(config)
