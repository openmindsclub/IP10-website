<template>
  <div id="activities" class="about">
    <h2>About US</h2>
    <img class="clubLogo" src="../assets/omc_logo_white.png"/>
    <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Repudiandae natus, sint enim optio et unde esse doloremque labore, repellendus quod itaque similique fuga odio ad, odit aliquid culpa saepe ab.</p>
    <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
  </div>
</template>

<style scoped >
.about{
    background-image: url("../assets/backgrounds/club_background.png");

    height: 100vh;
    width: 100%;

    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    position: relative;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
}

h2{
    color: white;
    font-size: 70px;
    margin-top: 60px;
    margin-bottom: 30px;
}

.clubLogo{
    width:200px;
}

p{
    font-size: 17px;
    color: white;
    margin-top: 30px;
    margin-bottom: 20px;
    margin-left: 10%;
    margin-right: 10%;
}


@media(max-width: 765px){

    .about {
        height: fit-content;
        background-repeat: repeat;
    }
}


</style>
