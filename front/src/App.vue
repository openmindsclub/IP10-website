<template>
  <div>
      <transition :name="transition_name">
          <router-view></router-view>
      </transition>
  </div>
</template>

<script>

export default {
  name: 'App',
  data () {
    return {
      transition_name: 'slide-left'
    }
  },
  watch: {
      '$route' (to, from) {
          if (to.name == "Registration"){
              if (from.name == "Home"){
                  this.transition_name = "registration"
              } else if (from.name == "Acceuil"){
                  this.transition_name = "registration"
              }
          } else if (to.name == "Home"){
              if (from.name == "Registration"){
                  this.transition_name = "registration-go"
              } else if (from.name == "Acceuil"){
                  this.transition_name = "welcome-home"
              }
          } else if (to.name == "Acceuil"){
              if (from.name == "Registration"){
                  this.transition_name = "registration-go"
              } else if (from.name == "Home"){
                  this.transition_name = "home-welcome"
              } else if (from.name == null) {
                  this.transition_name = "null-welcome"
              }
          }
      }
  }
}
</script>

<style>

/* transition to registration route*/

.registration-leave-active {
    transition: all 2s ease-out;
    position: absolute;
}

.registration-enter-active {
    transition: all 2s ease-out;
    position: fixed;
}

.registration-enter {
    transform: translateX(100%);
}

.registration-leave-to {
    transform: translateX(-100%);
}

/* transition from registration route to home or welcome route*/
.registration-go-leave-active {
    transition: all 2s ease-out;
    position: absolute;
}

.registration-go-enter-active {
    transition: all 2s ease-out;
    position: absolute;
}

.registration-go-enter {
    transform: translateX(-100%);
}

.registration-go-leave-to {
    transform: translateX(100%);
}

@keyframes moveFromReg {
    0% {
        transform: translateX(0);
    }
    100% {
        transform: translateX(100%);
    }
}

@keyframes moveToReg {
    0% {
        transform: translateX(-100%);
    }
    100% {
        transform: translateX(0);
    }
}

/* transition from welcome route to home route*/

.welcome-home-enter-active, .welcome-home-leave-active {
    animation: moveUp 0.9s ease-in;
}


@keyframes moveUp {
    0% {
        transform: translateY(0);
    }
    100% {
        transform: translateY(-100vh);
    }
}


/* transition from home route to welcome route*/

.home-welcome-enter-active {
    animation: moveDownWelcome 0.9s ease-in;
    position: absolute;
}

.home-welcome-leave-active {
    animation: moveDownHome 0.9s ease-in;
    position: fixed;
}

@keyframes moveDownHome {
    0% {
        transform: translateY(0);
    }
    100% {
        transform: translateY(100vh);
    }
}

@keyframes moveDownWelcome {
    0% {
        transform: translateY(-100vh);
    }
    100% {
        transform: translateY(0);
    }
}

/* transition to welcome route*/


</style>
