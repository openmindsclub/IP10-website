<template>
    <div id="activities" class="hero">

        <div class="page">
            <div class="battle-graphic">
                <Paragraph title="Battle Graphique" content="Vous êtes un designer en herbe et vous voulez vous mettre au défi ? Pourquoi donc ne pas participer à la battle graphique ? Votre challenge ? Mettre en scène Tux notre mascotte dans un de nos designs." color="gray"/>
            </div>
            <div class="tresor-hunt">
                <Paragraph title="Chasse au Tresor" content="Un trésor est caché à l’USTHB, réussirez-vous à le trouver ? Nous vous invitons à participer a cette epic aventure ou vous devriez résoudre des énigmes et trouver des indices, dans le but de trouver le trésor cacher à l’USTHB durant l’événement."/>
            </div>
        </div>
    </div>
</template>

<script>
import Paragraph from '../components/Paragraph.vue'
export default {
    name: "Activities",
    components: {
        Paragraph
    },
};
</script>


<style scoped >
.hero{
    background-image: url("../assets/backgrounds/activities_background.jpg");

    height: 100vh;
    width: 100%;

    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    position: relative;

    display: flex;
    flex-direction: column;
}

.page{
    padding-left: 5%;
    padding-top:4%;
    padding-right: 5%;
    width: 100%;
    height: 100%;
}

.battle-graphic{
    width: 360px;
    position: absolute;
    top: 30px;
    left: 30px;
}

.tresor-hunt{
    width: 360px;
    position: absolute;
    bottom: 30px;
    right: 30px;
}

@media(max-width: 800px){
    .battle-graphic{
        width: 300px;
        top: 20px;
        left: 20px;
    }

    .tresor-hunt{
        width: 300px;
        bottom: 20px;
        right: 20px;
    }
}

@media(max-width: 650px){
    .battle-graphic{
        width: 250px;
        top: 10px;
        left: 10px;
    }

    .tresor-hunt{
        width: 250px;
        bottom: 10px;
        right: 10px;
    }
}

@media(max-width: 530px){
    .battle-graphic{
        width: 200px;
        top: 5px;
        left: 5px;
    }

    .tresor-hunt{
        width: 200px;
        bottom: 5px;
        right: 5px;
    }
}

@media(max-width: 500px){
    .page{
        display: flex;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
    }

    .battle-graphic{
        position: relative;
        width: 80%;
    }

    .tresor-hunt{
        position: relative;
        width: 80%;
    }
}
</style>
