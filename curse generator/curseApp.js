'use strict';

angular.module('curseApp', [])
.controller('MainController', function($scope){
$scope.getRandomIndex = function(length){
    return Math.floor(Math.random() * length);
};
    $scope.words = [
        {
            value: 'kutya'
        },
        {
            value: 'cica'
        },
        {
            value: 'maci'
        },
        {
            value: 'laci'
        },
        {
            value: 'penis'
        },
        {
            value: 'kids'
        },

    ];
});
