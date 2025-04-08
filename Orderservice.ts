import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ApiService } from '../../../services/api.service';

@Component({
  selector: 'app-connect',
  templateUrl: './connect.component.html',
  styleUrls: ['./connect.component.css']
})
export class ConnectComponent implements OnInit {
  form!: FormGroup;
  data: any[] = [];
  columns: string[] = [];
  error: string | null = null;

  constructor(
    private fb: FormBuilder,
    private api: ApiService
  ) {}

  ngOnInit() {
    // build the reactive form
    this.form = this.fb.group({
      orderNumber: ['', Validators.required]
    });
  }

  onSearch() {
    // reset state
    this.error = null;
    this.data = [];

    if (this.form.invalid) {
      this.error = 'Please enter an order number';
      return;
    }

    const orderNumber = this.form.value.orderNumber;
    this.api.searchOrders(orderNumber).subscribe({
      next: (res: any[]) => {
        this.data = res;
        // grab columns from the first object
        this.columns = res.length ? Object.keys(res[0]) : [];
      },
      error: err => {
        this.error = err.message || 'Error fetching orders';
      }
    });
  }
}
