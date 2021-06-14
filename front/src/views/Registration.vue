<template>
    <div class="back">
        <div class="elevated-form">
            <b-form @submit="onSubmit" @reset="onReset">
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
                        v-model="form.lastName"
                        required
                    ></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-3" label="Prenom:" label-for="input-3">
                    <b-form-input
                        id="input-3"
                        v-model="form.firstName"
                        required
                    ></b-form-input>
                </b-form-group>

                <b-form-group id="input-group-4" label="Date de Naissance:" label-for="input-4">
                    <b-form-datepicker
                        id="input-4"
                        v-model="form.birthDate" :min="min" :max="max"
                        locale="fr"
                        class="mb-2"
                        required
                    ></b-form-datepicker>
                </b-form-group>

                <b-form-group id="input-group-5" label="Choisissez les conferences auquels vous voullez participer" v-slot="{ ariaDescribedby }" label-for="input-5">
                    <b-form-checkbox-group
                        id="input-5"
                        v-model="form.selectedConfs"
                        :options="conferences"
                        :aria-describedby="ariaDescribedby"
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

                <b-form-group id="input-group-7" label="Voulez vous participer a la chasse au tresor" v-slot="{ ariaDescribedby }" label-for="input-7">
                    <b-form-checkbox-group
                        id="input-7"
                        v-model="form.tresorHunt"
                        :options="tresorHunt"
                        :aria-describedby="ariaDescribedby"
                        name="flavour-2a"
                        stacked
                    ></b-form-checkbox-group>
                </b-form-group>


                <b-form-group id="input-group-8" label="Etes vous un etudiants de l'USTHB" label-for="input-8">
                    <b-form-radio-group
                        id="input-8"
                        v-model="form.USTHBStudent"
                        :options="USTHBStudent"
                        :aria-describedby="ariaDescribedby"
                        name="radio-options"
                        required
                    ></b-form-radio-group>
                </b-form-group>

                <b-form-group id="input-group-9" label="Dans Quel université etes vous inscrit?" label-for="input-9">
                    <b-form-input
                        id="input-9"
                        v-model="form.wichUniversity"
                        required
                    ></b-form-input>
                </b-form-group>

                <b-button type="submit" variant="primary">Submit</b-button>
                <b-button type="reset" variant="danger">Reset</b-button>
            </b-form>
            <b-card class="mt-3" header="Form Data Result">
                <pre class="m-0">{{ form }}</pre>
            </b-card>
        </div>
    </div>
</template>

<script>
export default {
  name: "Registration",
  data() {
      const minDate = new Date(1970, 1, 1);
      const maxDate = new Date(2004, 11, 31);
      return {
        form: {
          email: '',
          firstName: '',
          lastName: '',
          birthDate: '',
          selectedConfs: [],
          activity: null,
          tresorHunt: null,
          USTHBStudent: null,
          wichUniversity: ''
        },
        activities: [
          { value: null, text: 'Aucune' },
          { value: 'battleGraphique', text: 'La Battle Graphique' },
          {
            label: 'Workshops',
            options: [
              { value: 'Python', text: 'Machine Learning avec Python' },
              { value: 'Godot', text: 'Godot' }
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
        ],
        min: minDate,
        max: maxDate,
        show: true
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        alert(JSON.stringify(this.form))
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values

        this.form.email = ''
        this.form.firstName = ''
        this.form.lastName = ''
        this.form.birthDate = ''
        this.form.activity = null
        this.form.USTHBStudent = null
        his.form.tresorHunt = null
        this.form.selectedConfs = []
        this.form.wichUniversity = ''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
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
    width: 90%;

    border-radius: 25px;
    background-color: white;
    opacity: 0.8;

    padding: 20px;

    overflow-y: scroll;
}
</style>
