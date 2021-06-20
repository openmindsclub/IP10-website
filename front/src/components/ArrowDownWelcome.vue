<template>
    <div class="footer-screen">
        <h6>{{ title }}</h6>
        <router-link to="Home"><i class="fas fa-angle-down"></i></router-link>
    </div>
</template>

<script>
export default {
  name: "ArrowDownWelcome",
  props: ['title'],
};
</script>

<style scoped >

.footer-screen{
    justify-content: center;
    align-items: center;
    padding: 0px;
    height: 90px;
    width: 100%;
    display: flex;
    flex-direction: column;
    position: fixed;
    padding: 10px 10px 10px 10px;
    bottom: 1em;
}

h6{
    font-size: 1em;
    color: #4B535C;
    font-weight: bold;
    margin: 0;
    padding: 0;
    position: relative;
    top: 0.9em;
    left: 0.5em;
}

a{
    line-height:34px;
    color: #4B535C;
    height:34px;
    width:34px;
    font-size:4.3em;
    margin: 0;
    padding: 0;
}

.footer-screen:hover a, .footer-screen:hover h6{
    color: #69B370;
    animation-name: wooble;
    animation-duration: 4s;
    animation-iteration-count: infinite;
}

@keyframes wooble {
    0%{transform: translateY(0px);}
    60%{transform: translateY(-30px);}
    100%{transform: translateY(0px);}
}

@media (max-width: 600px){
    .footer-screen{
        position: relative;
        padding: 0;
        bottom: 3em;
    }
}

</style>
