// src/app/components/software-service/connect/connect.component.ts
import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { OrderService } from '../../../services/order.service';

@Component({
  selector: 'app-connect',
  templateUrl: './connect.component.html'
})
export class ConnectComponent implements OnInit {
  form!: FormGroup;
  data: any[] = [];
  error: string | null = null;

  constructor(
    private fb: FormBuilder,
    private orderSvc: OrderService
  ) {}

  ngOnInit() {
    this.form = this.fb.group({
      orderNumber: ['', Validators.required]
    });
  }

  onSearch() {
    this.error = null;
    this.data = [];

    if (this.form.invalid) {
      this.error = 'Order number is required';
      return;
    }

    const num = this.form.value.orderNumber;
    this.orderSvc.searchByPost(num).subscribe({
      next: results => {
        this.data = results;
      },
      error: err => {
        this.error = err.message || 'Failed to fetch order';
      }
    });
  }
}
