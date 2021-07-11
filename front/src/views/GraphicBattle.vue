<template>
    <div class="reg-container">
        <NavBar route="registration"/>
        <b-container fluid class="back">
            <b-row class="elevated-form" align-v="center">
                <b-col xl="12">
                    <b-form @submit="onSubmit" @reset="onReset">

                            <b-form-group id="input-group-1" label="Addresse email :" label-for="input-1">
				<b-form-input
                                    id="input-1"
                                    v-model="form.email"
                                    type="email"
                                    required
                                ></b-form-input>
                            </b-form-group>
				<b-form-group id="input-group-1" label="Lien vers le drive contenant votre design :" label-for="input-1">
                                <b-form-input
                                    id="input-1"
                                    v-model="form.link"
                                    type="text"
                                    required
                                ></b-form-input>
                            </b-form-group>
			<b-row align-h="around">
                            <b-col  >
                                <b-button type="submit" variant="primary">Submit</b-button>
                            </b-col>
                            <b-col >
                                <b-button type="reset" variant="danger" >Reset</b-button>
                            </b-col>
                        </b-row>
                    </b-form>
                </b-col>
            </b-row>
        </b-container>
<b-modal v-model="showModal" id="modal-success" centered :title="modalHeading">
            <p class="my-4">{{modalText}}</p>
            <template v-if="sucess" #modal-footer="{ok}">
                <b-button @click="ok()" size="sm" variant="success">Take me Home</b-button>
            </template>
            <template v-else  #modal-footer="{ok}">
                <b-button @click="ok()" size="sm">OK</b-button>
            </template>
        </b-modal>
    </div>
</template>

<script>
import $backend from '../backend'
import NavBar from '../components/NavBar'

export default {
  name: "GraphicBattle",
  component: {
      NavBar,
  },
  data() {
      return {
        form: {
          email: "",
          link:"",
        },
// modal
        showModal: false,
        modalHeading: "",
        modalText: "",
        modalTheme: "",
	sucess:false,
	loading:false,
        show: true,
        errored: false,
        error : "",
	};
},
    methods: {
      onSubmit(event) {
        event.preventDefault()
        this.sucess = false
        this.loading = true

        $backend.graphicBattle(this.form)
        .then(responseData => {
            this.info = responseData
        }).catch(error => {
            this.errored = true
            this.error = error.message
        })
        .finally(() =>{
            this.loading = false
            if ('success' in this.info){
                this.modalHeading =  "Votre travail a bien etais soumit"
                this.modalText = "felicitation, votre travail a bien etais soumit, en attendant n'hesiter pas à participer à nos autres activités"
                this.modalTheme = ""
                this.showModal = true
                this.sucess = true
            } else if ('error' in this.info) {
                this.sucess = false
                this.modalHeading =  "Un probleme est survenue au cours de la soumissions veuillez reasseyer"
                this.modalText = this.info["error"]
                this.modalTheme = ""
                this.showModal = true
            } else {

            }
        })
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values

        this.form.email = ''
        this.form.first_name = ''
        this.form.last_name = ''
        this.form.workshops = ''
        this.form.isUSTHB = null
        this.form.tresor_hunt = false
        this.form.battle_graphique = false
        this.form.conferences = []
        this.form.which_university = ''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      },
      toggleModal() {
          this.showModal = false
      },
      Navigate() {
          if (this.sucess){
              this.sucess = false
              this.$router.push({path: '/'})
          }
      }

    },
    computed: {
        showWichUniversity(){
            if (this.form.isUSTHB == null || this.form.isUSTHB){
                return false
            } else {
                return true
            }
        }
    },
    mounted() {
    this.$root.$on('bv::modal::hide', (bvEvent, modalId) => {
      if (this.sucess){
          this.Navigate()
      }
    })
  }
};
</script>


<style scoped >

.reg-container{
    width: 100%;
}

.back{
    background-image: url("../assets/backgrounds/Event_background_2.jpg");

    height: 100vh;
    width: 100%;

    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;

    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
}

.elevated-form{
    height: 85vh;

    border-radius: 25px;
    background-color: white;
    opacity: 0.8;

    padding: 20px;
}

.to-scroll{
    height: 70vh;
    padding: 20px;
    margin-bottom: 10px;
    overflow-y: scroll;
}
::-webkit-scrollbar {
  width: 10px;
}

::-webkit-scrollbar-track {
  background: #f1f1f1;
  border-radius: 25px;
}

::-webkit-scrollbar-thumb {
  background: #888;
  border-radius: 25px;
}

::-webkit-scrollbar-thumb:hover {
  background: #555;
}

@media(max-width: 910px){
    .elevated-form{
        padding: 5px;
        margin: 20px;
    }
}

@media(max-height: 750px){
    .elevated-form{
        padding: 5px;
        margin-top: 50px;
    }

    .to-scroll{
        height: 70vh;
        padding: 20px;
 }
}

@media(max-height: 500px){

    .elevated-form{
        padding-left: 10px;
    }

    .to-scroll{
        height: 67vh;
    }
}

@media(max-height: 321px){

    .elevated-form{
        height: 79vh;
    }

    .to-scroll{
        height: 55vh;
    }
}

</style>
