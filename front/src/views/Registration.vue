<template>
    <div>
        <NavBar route="registration"/>
        <b-container fluid class="back">
            <b-row class="elevated-form" align-v="center">
                <b-col xl="12">
                    <b-form @submit="onSubmit" @reset="onReset">

                        <div class="to-scroll">
                            <b-form-group id="input-group-1" label="Email address:" label-for="input-1">
                                <b-form-input
                                    id="input-1"
                                    v-model="form.email"
                                    type="email"
                                    placeholder="Enter email"
                                    required
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group id="input-group-2" label="Nom:" label-for="input-2">
                                <b-form-input
                                    id="input-2"
                                    v-model="form.last_name"
                                    required
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group id="input-group-3" label="Prenom:" label-for="input-3">
                                <b-form-input
                                    id="input-3"
                                    v-model="form.first_name"
                                    required
                                ></b-form-input>
                            </b-form-group>

                            <b-form-group id="input-group-4" label="Date de Naissance:" label-for="input-4">
                                <b-form-datepicker
                                    id="input-4"
                                    v-model="form.birth_date" :min="min" :max="max"
                                    locale="fr"
                                    class="mb-2"
                                    required
                                ></b-form-datepicker>
                            </b-form-group>

                            <b-form-group id="input-group-5" label="Choisissez les conferences auquels vous voullez participer" label-for="input-5">
                                <b-form-checkbox-group
                                    id="input-5"
                                    v-model="form.conferences"
                                    :options="conferences"
                                    name="flavour-2a"
                                    stacked
                                ></b-form-checkbox-group>
                            </b-form-group>

                            <b-form-group id="input-group-6" label="Dans quels activitées aimeriez vous participer?" label-for="input-6">
                                <b-form-select
                                    id="input-6"
                                    v-model="form.activities"
                                    :options="activities"
                                ></b-form-select>
                            </b-form-group>

                            <b-form-group id="input-group-7" label="Voulez vous participer a la chasse au tresor" label-for="input-7">
                                <b-form-radio-group
                                    id="input-7"
                                    v-model="form.tresor_hunt"
                                    :options="tresorHunt"
                                ></b-form-radio-group>
                            </b-form-group>


                            <b-form-group id="input-group-8" label="Etes vous un etudiants de l'USTHB" label-for="input-8">
                                <b-form-radio-group
                                    id="input-8"
                                    v-model="form.isUSTHB"
                                    :options="USTHBStudent"
                                    name="radio-options"
                                    required
                                ></b-form-radio-group>
                            </b-form-group>

                            <b-form-group v-if="showWichUniversity" id="input-group-9" label="Dans Quel université etes vous inscrit?" label-for="input-9">
                                <b-form-input
                                    id="input-9"
                                    v-model="form.which_university"
                                    required
                                ></b-form-input>
                            </b-form-group>
                        </div>

                        <b-row align-h="around">
                            <b-col  >
                                <b-button type="submit" variant="primary">Inscrivez Vous</b-button>
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
  name: "Registration",
  component: {
      NavBar,
  },
  data() {
      const minDate = new Date(1970, 1, 1);
      const maxDate = new Date(2004, 11, 31);
      return {
        form: {
          email: '',
          first_name: '',
          last_name: '',
          birth_date: '',
          conferences: [],
          activities: null,
          tresor_hunt: null,
          isUSTHB: null,
          which_university: ''
        },
        activities: [
          { value: null, text: 'Aucune' },
          { value: 'battle_graphique', text: 'La Battle Graphique' },
          {
            label: 'Workshops',
            options: [
              { value: 'python', text: 'Machine Learning avec Python' },
              { value: 'godot', text: 'Godot' }
            ]
          }
        ],
        conferences: [
          { text: "Ceremonie d'ouverture & Différence entre libre opensource", value: 'conference1' },
          { text: "L'open source dans le développement scientifique et les nouvelle technologies ", value: 'conference2' },
          { text: "L'Avenir de l'open source dans le développement des nouvelles technologie en algérie et dans le monde", value: 'panel1' },
          { text: "Géant de l'industrie qui se tourne vers l'open source ", value: 'conference3' },
          { text: "Comment l'open source peut améliorer la croissance des entreprises en Algérie", value: 'panel2' }
        ],
        USTHBStudent: [
          { text: "oui", value: true },
          { text: "non", value: false },
        ],
        tresorHunt: [
          { text: "oui", value: true },
          { text: "non", value: false },
        ],
        min: minDate,
        max: maxDate,
        show: true,
        loading : false,
        errored: false,
        error : "",

        // modal
        showModal: false,
        sucess: false,
        modalHeading: "",
        modalText: "",
        modalTheme: "",
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        this.sucess = false
        this.loading = true

        $backend.registration(this.form)
        .then(responseData => {
            this.info = responseData
        }).catch(error => {
            this.errored = true
            this.error = error.message
        })
        .finally(() =>{
            this.loading = false
            console.log(this.info)
            if ('success' in this.info){
                this.modalHeading =  "Inscription reussite"
                this.modalText = "Felicitation vous avez reussit à vous inscrire à l'install party 10"
                this.modalTheme = ""
                this.showModal = true
                this.sucess = true
            } else if ('error' in this.info) {
                this.modalHeading =  "Un probleme est survenue au cours de l'inscription"
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
        this.form.birth_date = ''
        this.form.activities = null
        this.form.isUSTHB = null
        this.form.tresor_hunt = null
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
          this.$router.push({path: '/'})
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
.back{
    background-image: url("../assets/backgrounds/Event_background_2.jpg");

    height: 100vh;
    width: 100%;

    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
    position: relative;

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

/* width */
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
        margin-bottom: 10px;
        overflow-y: scroll;
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
