// src/app/services/order.service.ts
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable } from 'rxjs';
import { AuthService } from '../auth.service';

@Injectable({ providedIn: 'root' })
export class OrderService {
  private apiUrl = 'http://your-api-host/api/orders';

  constructor(
    private http: HttpClient,
    private auth: AuthService
  ) {}

  searchOrder(orderNumber: string): Observable<any[]> {
    const token = this.auth.getToken();  // however you expose it
    const headers = new HttpHeaders().set('Authorization', `Bearer ${token}`);
    return this.http.get<any[]>(
      `${this.apiUrl}?orderNumber=${encodeURIComponent(orderNumber)}`,
      { headers }
    );
  }
}
