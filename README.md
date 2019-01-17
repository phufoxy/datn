# Đồ Án Tốt Nghiệp
# Backend
# User =>
    1) Login #
    2) Register #
    3) Forget Password
    4) Remenber Password
    5) Logout #
# Places => 
    1) Places: 
        . Create and select all #
            . dashboard: authentication IsAuthenticated #
            . Home: authentication IsAuthenticatedOrReadOnly
        . Update and Delete and GET id #
            . dashboard: authentication IsAuthenticated
        . Select Max , min price 
            . Home: authentication IsAuthenticatedOrReadOnly
    2) Place Details 
        . Create and select all
            . dashboard: authentication IsAuthenticated #
            . Home: authentication IsAuthenticatedOrReadOnly
        . Update and Delete and Get Id
            . dashboard: authentication isToken #
    3) Join Places and Details
        . Select join 2 table #
    4) Comment Places
        . Create and select all
            . dashboard: authentication IsAuthenticated
            . Home: authentication Allow Any
# Hotels =>
    1) Hotel
        . Create and select all #
            . dashboard: authentication IsAuthenticated #
            . Home: authentication IsAuthenticatedOrReadOnly
        . Update and Delete and GET id #
            . dashboard: authentication IsAuthenticated
        . Select Max , min price 
            . Home: authentication IsAuthenticatedOrReadOnly
    2) Hotel Details
        . Create and select all
            . dashboard: authentication IsAuthenticated #
            . Home: authentication IsAuthenticatedOrReadOnly
        . Update and Delete and Get Id
            . dashboard: authentication isToken #
    3) Comment 
        . Create and select all
            . dashboard: authentication IsAuthenticated
            . Home: authentication Allow Any