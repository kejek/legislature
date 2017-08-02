// Code goes here
angular.module('mainApp', ['apiFactory'])
  .controller('mainCtrl', function($scope, $interval, $http, apiFactory) {
	 $scope.employeeURI = '/employee/';
	 $scope.employeeList = [];
     $scope.createWorker = function() {

      var findByEmployeeId = function(id) {
        apiFactory.findByEmployeeId($scope, id);
      };
	  
	  var findAllEmployees = function() {
		  apiFactory.findAllEmployees($scope);
	  };
      
		findAllEmployees();

      return {
        findByEmployeeId: findByEmployeeId,
        findAllEmployees: findAllEmployees
      };
    };

    $scope.worker = $scope.createWorker();
  });
