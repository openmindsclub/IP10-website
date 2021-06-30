<template>
  <div id="about" class="about">
    <h2>About US</h2>
    <img class="clubLogo" src="../assets/omc_logo_white.png"/>
    <p>Nous, <em>OpenMindsClub</em> sommes un club scientifique de l’USTHB fonder en Mars 2009 suite à une organisation réussie de la première install party à l'université par un groupe d'étudiants et enseignants.</p>
    <p>Nous, OpenMindsClub sommes un club scientifique de l’USTHB, ayant comme philosophie le libre, l’open source et l’esprit de partage, notre objectif est de promouvoir ces derniers en organisant des événements, formations et autre manifestation scientifique. Bien sûr, en tant que promoteur de l’esprit de partage notre objectif est aussi de transmettre notre savoir et connaissance au maximum de gens possible, car comme notre slogan le dit si bien <em>"ce qui ne se partage pas se perd"</em>.</p>
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
