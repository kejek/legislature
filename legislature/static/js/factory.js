angular.module('apiFactory', [])
  .factory('apiFactory', function($http) {

    var factory = {};
    
    
    factory.findByEmployeeId = function($scope, id) {
      $http.get($scope.employeeURI + id)
        .success(function(response) {
		  $scope.employeeList = [];
          $scope.employeeList.push(response[0]) ;
          $scope.getEmployeeError = null;
        })
        .error(function() {
          $scope.getEmployeeError = "Unable to get Employee Data!";
        });
    };
	
	factory.findAllEmployees = function($scope) {
      $http.get($scope.employeeURI)
        .success(function(response) {
		  $scope.employeeList = [];
		  for(i = 0; i < response.length; i++){
			$scope.employeeList.push(response[i]) ;
		  }
          $scope.getEmployeeError = null;
        })
        .error(function() {
          $scope.getEmployeeError = "Unable to get Employee Data!";
        });
    };
    
    
    return factory;
  });