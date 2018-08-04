from django.test import TestCase
from django.shortcuts import reverse
from project.models import ProjectDetail
from nsp.tests import TestLoginRequired
from project.issueSolution.models import Issue,IssueComment,Solution,SolutionComment
from django.contrib.auth.models import User

# Create your tests here.

class TestIssueSolutionViewsLoginRequired(TestLoginRequired):
	def setUp(self):
		self.user_object = User.objects.create(username="testing",
												password="testing")
		self.project_object = ProjectDetail.objects.create(project_name="testing",
															initiated_by=self.user_object,
															mentor_name="testing",
															branch="testing",
															description="testing")
		self.issue_object = Issue.objects.create(user=self.user_object,
												project=self.project_object,
												title="testing",
												description="testing")
		self.solution_object = Solution.objects.create(issue=self.issue_object,
														user=self.user_object,
														title="testing",
														description="testing")
		self.issueComment_object = IssueComment.objects.create(issue=self.issue_object,
																user=self.user_object,
																comment="testing")
		self.solutionComment_object = SolutionComment.objects.create(solution=self.solution_object,
														user=self.user_object,
														comment="testing")
		################# args for paths
		deleteIssueSolution_args = ["issue",self.solution_object.id]
		projectIssues_args = [self.project_object.id,"open"]
		projectSolutions_args = [self.project_object.id,"open"]
		commentIssueSolution_args = [self.project_object.id,"issue",self.issue_object.id]
		editIssueSolution_args = [self.project_object.id,"issue",self.issue_object.id]
		createIssueSolution_args = [self.project_object.id,"issue"]
		viewIssueSolution_args = [self.project_object.id,"issue",self.issue_object.id]
		changeStatusIssueSolution_args = [self.project_object.id,"issue",self.issue_object.id,"open"]
		######
		self.pathnames_args = {"deleteIssueSolution":deleteIssueSolution_args,"projectIssues":projectIssues_args,
								"projectSolutions":projectSolutions_args,"commentIssueSolution":commentIssueSolution_args,
								"editIssueSolution":editIssueSolution_args,"createIssueSolution":createIssueSolution_args,
								"changeStatusIssueSolution":[self.project_object.id,"issue",self.issue_object.id,"open"],
								"viewIssueSolution":viewIssueSolution_args}