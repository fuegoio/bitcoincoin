<template>
  <div>
    <span class="title font-weight-bold">Posologie limite</span>
    <v-row class="align-center grey--text text--darken-5" dense>
      <v-col cols="12" class="d-flex align-center">
        <div class="text-no-wrap mx-1">Une prise de</div>
        <v-text-field
          v-model="posologyDosage"
          class="mx-1"
          type="number"
          label="Dose"
          placeholder="..."
          reverse
          prefix="mg"
        ></v-text-field>
        <div class="text-no-wrap mx-3">max. toutes les</div>
        <v-text-field
          v-model="posologyFrequencyValue"
          class="mx-1"
          type="number"
          label="Fréquence"
          placeholder="..."
          reverse
        ></v-text-field>
        <v-select
          v-model="posologyFrequencyUnit"
          :items="availableFrequencies"
          item-text="label"
          item-value="value"
          class="mx-1"
        ></v-select>
      </v-col>
    </v-row>
    <span class="title font-weight-bold">... lorsque le patient est</span>
    <v-row class="mt-3">
      <v-col v-for="choices in availablePatientPredicate" :key="choices.label">
        <PatientPredicateSelector
          :label="choices.label"
          :items="choices.items"
          item-label="label"
          item-value="value"
          @change="updatePatientPredicates(choices.label, $event)"
        ></PatientPredicateSelector>
      </v-col>
    </v-row>
  </div>
</template>

<script lang="ts">
import { Component, Prop, Vue } from 'vue-property-decorator'

import PatientPredicateSelector from '@/components/patients/PatientPredicateSelector.vue'
import { PatientPredicateDefinitions } from '@/models/patient'
import {
  FrequencyUnitDefinition,
  FrequencyUnitDefinitions,
} from '@/models/drugs'
import { Rule } from '@/models/rules'

@Component({ components: { PatientPredicateSelector } })
export default class OverdoseDetailsTemplate extends Vue {
  @Prop() public value!: Rule

  public posologyDosage = ''
  public posologyFrequencyValue = ''
  public posologyFrequencyUnit = ''

  public patientPredicates: any = {}

  public get availablePatientPredicate(): object[] {
    const predicatesByCategory: any = {}
    PatientPredicateDefinitions.forEach(predicate => {
      if (predicatesByCategory[predicate.category] === undefined) {
        predicatesByCategory[predicate.category] = []
      }
      predicatesByCategory[predicate.category].push({
        label: predicate.label,
        value: predicate.value,
      })
    })
    return Object.keys(predicatesByCategory).map(category => {
      return { label: category, items: predicatesByCategory[category] }
    })
  }

  public get availableFrequencies(): FrequencyUnitDefinition[] {
    return FrequencyUnitDefinitions
  }

  public updatePatientPredicates(
    category: string,
    predicate: { value: string } | null,
  ): void {
    if (predicate !== null) {
      this.patientPredicates[category] = predicate.value
    } else {
      this.patientPredicates[category] = undefined
    }
  }
}
</script>

<style scoped></style>
