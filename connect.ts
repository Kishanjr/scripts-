// src/app/components/software-service/connect/connect.module.ts
import { NgModule }             from '@angular/core';
import { CommonModule }         from '@angular/common';
import { ReactiveFormsModule }  from '@angular/forms';
import { ConnectComponent }     from './connect.component';

@NgModule({
  declarations: [
    ConnectComponent
  ],
  imports: [
    CommonModule,
    ReactiveFormsModule   // ← add this
  ]
})
export class ConnectModule {}
