<template>
  <v-card class="pa-2">
    <v-row class="align-center">
      <v-col cols="1" class="d-flex justify-center">
        <v-icon large>mdi-check</v-icon>
      </v-col>
      <v-col cols="8">{{ rule.name }}</v-col>
      <v-col cols="2">
        <span class="grey--text font-weight-bold"
          >Gravité :
          <span class="font-weight-light">{{ ruleGravityLabel }}</span></span
        >
      </v-col>
      <v-col cols="1" class="d-flex justify-center">
        <v-icon>mdi-pencil</v-icon>
      </v-col>
    </v-row>
  </v-card>
</template>

<script lang="ts">
import { Vue, Component, Prop } from 'vue-property-decorator'

import {
  Rule,
  RuleGravityDefinition,
  RuleGravityDefinitions,
} from '@/models/rules'

@Component({})
export default class RuleCard extends Vue {
  @Prop({ required: true }) public rule!: Rule

  public get ruleGravityLabel(): string {
    const ruleGravity = RuleGravityDefinitions.find(
      (gravity: RuleGravityDefinition) => gravity.key === this.rule.gravity,
    )
    if (ruleGravity !== null && ruleGravity !== undefined) {
      return ruleGravity.label
    }
    return 'Inconnue'
  }
}
</script>

<style lang="scss" scoped></style>
